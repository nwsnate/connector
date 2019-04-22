# Connector

Remote server administration and listing for the terminal.

### Installation

- Clone the repository: `git clone https://github.com/nwsnate/connector.git ~/connector/`

- Set up the alias: `echo "alias c='python3 ~/connector/connect.py'" >> ~/.zshrc` (Or `~/.bashrc` if your still using bash.)

- Set up your `~/.conrc` file. This should use the format `server-name:connection command`. 1 machine per line. You can even run other commands like remmina for VNC/RDP.

  ```text
  orion:ssh nate@orion.local
  router:ssh nate@10.0.0.1
  windows:remmina -c /home/nate/.remmina/8675309.remmina
  ```

 - Edit `connect.py` to reflect the location of your `.conrc` file.

### Usage

- Run connection command: `c server-name`

- List servers: `c list`

  The following functions only work in UNIX. If you want you can change this.

- Ping: `c ping server-name`

- Traceroute: `c trace server-name`


### Contributing

This is an open source project, so feel free to contact me or submit pull requests anytime you like.


### License
GNU GPLv3
