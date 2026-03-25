# astrbot_piugin_help_image_reply
一个用于 AstrBot 的简单插件：当用户发送 `/help` 指令时，机器人自动回复一张自定义帮助图片。适用于菜单展示、帮助说明、群功能介绍、指令面板等场景。该插件由GPT-5.4-codex-max编译。

---

## 功能特性

- 监听 `/help` 指令
- 自动回复本地图片
- 轻量、简单、即装即用
- 不依赖额外第三方 Python 库
- 适合作为 AstrBot 图片菜单插件模板

---

## 效果说明

用户发送：

`/help `

机器人回复：
assets/help.png
即插件目录中的帮助图片。

---

## 目录结构

```text
help_image_reply/
├─ main.py
├─ metadata.yaml
├─ requirements.txt
├─ README.md
└─ assets/
   └─ help.png
```

## 安装方法

将插件目录放入 AstrBot 的插件目录中：

```text
AstrBot/data/plugins/help_image_reply
```

确保图片文件存在：

```text
AstrBot/data/plugins/help_image_reply/assets/help.png
```

然后重载或重启 AstrBot，使插件生效。

## 使用方法

在聊天中发送以下指令：

```text
/help
```

机器人会自动回复本地图片。

## 快速开始

### 1. 放置插件

把整个 `help_image_reply` 文件夹放到：

```text
AstrBot/data/plugins/
```

### 2. 检查图片资源

确认图片存在于：

```text
assets/help.png
```

### 3. 启动或重载插件

启动 AstrBot，或在管理界面中重载插件。

### 4. 测试指令

发送：

```text
/help
```

如果配置正确，机器人会返回帮助图片。
```

