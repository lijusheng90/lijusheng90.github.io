# 服务器 mail消息 异常报错


##  问题

页面报错

```
new_emails, new_recipients_nbr =self._notify_send(fol_values['body'],fol_values['subject'],recipient_template_values['folowers'], **base_mail_values)
```
说这一句没有'body'


后台报错
```
mako_env = mako_safe_template_env if self.env.context.get('safe') else mako_template_env
```
不存在  mako_template_env

## 解决

```
try:
    # We use a jinja2 sandboxed environment to render mako templates.
    # Note that the rendering does not cover all the mako syntax, in particular
    # arbitrary Python statements are not accepted, and not all expressions are
    # allowed: only "public" attributes (not starting with '_') of objects may
    # be accessed.
    # This is done on purpose: it prevents incidental or malicious execution of
    # Python code that may break the security of the server.
    from jinja2.sandbox import SandboxedEnvironment
    mako_template_env = SandboxedEnvironment(
        block_start_string="<%",
        block_end_string="%>",
        variable_start_string="${",
        variable_end_string="}",
        comment_start_string="<%doc>",
        comment_end_string="</%doc>",
        line_statement_prefix="%",
        line_comment_prefix="##",
        trim_blocks=True,               # do not output newline after blocks
        autoescape=True,                # XML/HTML automatic escaping
    )
    mako_template_env.globals.update({
        'str': str,
        'quote': quote,
        'urlencode': urlencode,
        'datetime': datetime,
        'len': len,
        'abs': abs,
        'min': min,
        'max': max,
        'sum': sum,
        'filter': filter,
        'reduce': reduce,
        'map': map,
        'round': round,
        'cmp': cmp,

        # dateutil.relativedelta is an old-style class and cannot be directly
        # instanciated wihtin a jinja2 expression, so a lambda "proxy" is
        # is needed, apparently.
        'relativedelta': lambda *a, **kw : relativedelta.relativedelta(*a, **kw),
    })
    mako_safe_template_env = copy.copy(mako_template_env)
    mako_safe_template_env.autoescape = False
except ImportError:
    _logger.warning("jinja2 not available, templating features will not work!")

```

打印出来
_logger.warning("jinja2 not available, templating features will not work!")

说明 就在其中有异常

因为在本地ok
我试了下，from jinja2.sandbox import SandboxedEnvironment
没毛病
在服务其实报错

各个库都是有的
最后发现 MarkupSafe的版本有问题

pip list | grep MarkupSafe 
MarkupSafe (0.11)  

本地：
MarkupSafe (1.0)  


sudo pip uninstall MarkupSafe
sudo pip install MarkupSafe==1.0

重启odoo，ok
