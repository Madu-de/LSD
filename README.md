# LinuxShowDirector (LSD)

The Linux Show Director(LSD) is an open source project for everyone sick of GUI based presentation programs and who want to create a nice CLI presentation.

## How to use it
This project is linux only. We don't want to release a windows version because: why??

Step by step introduction:
- Use a good Linux Distro (not Ubuntu)
- Install python
    ```bash
    pacman -S python # https://wiki.archlinux.org/title/Python
    ```
- Make lsd executable
    ```bash
    sudo chmod +x lsd
    ```
- Run lsd
    ```bash
    ./lsd ./examples/presentation.lsd
    ```

## LSD File
### Syntax:
```lsd
shaderName["param1", 123, True];    <-- Shader call
<>                                  <-- Waiting for enter
```

### Default Shaders

#### TextShader
```lsd
text[
    x: double,
    y: double,
    width: double,
    text: str,
    layer: int,
    scale=1: int
]
```

#### BoxShader
```lsd
box[
    x: double,
    y: double,
    width: double,
    height: double,
    layer: int,
    scale=1: int
]
```

### Command Shaders

#### ColorShader
```lsd
color[
    backgroundColor: str,
    foregroundColor: str
]
```
Possible values for both: black, red, green, yellow, blue, magenta, cyan, light_gray, gray, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan, white

#### ClearShader
```lsd
clear[
    layer: int
]
```

#### StopAnimation
```lsd
stop_a[
    name: str
]
```

### Animations

#### LsdShader
```lsd
lsd[
    x: double,
    y: double,
    time_limit: double,
    delay: double,
    name: str,
    width: double,
    height: double,
    scale=1: int,
    full=False: bool
]
```

#### NextShader
```lsd
next[
    x: double,
    y: double,
    time_limit: double,
    delay: double,
    name: str    
]
```

## Contributors
- [LinuxShowDirector](https://github.com/LinuxShowDirector)
- [Madu-de](https://github.com/Madu-de)