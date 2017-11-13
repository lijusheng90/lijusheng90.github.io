# button 绑定一个瞬时模型的 act_window

1.在name里面按照如下格式进行
```
<header>
    <button string="Change Password" type="action" name="%(change_password_wizard_action)d" help="Change the user password."/>
</header>
```


```
<act_window id="change_password_wizard_actio"
name="Change Password"
src_model="res.users"
res_model="change.password.wizard"
view_type="form" 
view_mode="form"
key2="client_action_multi" 
target="new"
groups="base.group_erp_manager"/>
```