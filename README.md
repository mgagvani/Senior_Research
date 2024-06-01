This is the repository for Manav Gagvani's Senior Research Presentation with Dr. Gabor (SysLab) in 2023-2024.

Most information can be found in the Final Report. However, for those who would like to continue working with the car, here are some important details:

## Router
The Nvidia Jetson on the car, will, by default, connect to the router in Room 200C. The router does _not_ have internet access, despite the best efforts of the Sysadmins. You will need to connect to the router before you can SSH into the vehicle.

**Router IP Address:** `192.168.110.1`

**Jetson IP Address:** TODO (but you can also access it through selfdriving-jetson.lan)

For instance, here's the SSH config I'm using to remote in using VSCode remotes (it's already installed on the Jetson):
```rs
Host selfdriving-jetson
  HostName selfdriving-jetson.lan
  User selfdriving
```
For access to the Jetson's or router's passwords, **please message me.**
