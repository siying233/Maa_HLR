<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img alt="LOGO" src="maahlr_2026-02-25.png" width="256" height="256" />
</p>

<div align="center">

# MaaHLR

</div>

**MaaHLR**（海螺肉小助手）是一个基于 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 的《时空中的绘旅人》日常肝活小助手，通过**图像技术 + 模拟控制** ，解放双手！

## 免责条款

- 本项目仅为个人学习、研究和技术交流使用，不提供任何游戏资源篡改、破解内容或作弊功能。使用者请遵守游戏与平台相关条款。
- 本项目未与官方合作，不得在任何绘旅人官方渠道宣传MaaHLR。
- 基于本项目产生的任何违规使用、商业行为、法律责任，均由使用者自行承担，与项目作者及贡献者无关。
- 作者不承担因使用本项目导致的任何直接、间接、偶然、特殊或后果性损失，包括但不限于账号封禁、数据丢失、系统损坏、索赔纠纷等。
- 本资源为独立组件，其MIT许可证不传染，也不受与之集成的其他软件许可证的影响。

## 任务列表

- **🎮 启动绘旅人**：打开游戏（请确保模拟器已打开；第一次使用需要启动模拟器并登录账号）
- **💐 赠人玫瑰**：赠送好友体力
- **🎨 画展**：领取上一场画展奖励，并举办一场画展
- **🚶 课后出行**：出行并随机遇到男主，进行互赠礼物
- **📅 日程**：安排当天日常，优先邀请男主，随机邀请其他角色
- **🤹‍♀️ 画廊材料**：领取每日免费画廊材料
- **🎨 速写**：选择速写地点，连线灵感（图鉴持续完善中，未收录灵感请手动暂停）
- **🎁 奖励领取**：日常收尾，领取当日奖励

## 使用指南

- **Windows 10/11**
- **模拟器（推荐 MuMu）** 分辨率为 `1280*720` `320dpi`

- **运行安装** 解压后运行exe即可。

## 鸣谢

### 核心框架

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework)
  基于图像识别的自动化黑盒测试框架 | An automation black-box testing framework based on image recognition

### UI支持

- [MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia)
  基于 Avalonia UI 构建的 MaaFramework 通用 GUI 解决方案

### 开发者

感谢以下开发者对本项目作出的贡献：

- 本项目由 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 强力驱动
- 感谢所有贡献者：[Contributors](https://github.com/siying233/Maa_HLR/graphs/contributors)

<!-- ### 配置设备与任务

- **控制器配置示例**：`assets/config/maa_pi_config.json`
  - 其中包含 MuMu 的 `adb_path`、`address` 等示例配置，请按你的安装路径修改
- **流水线资源**：`assets/resource/pipeline/`
  - 文件分工可参考 `assets/resource/pipeline/readme.md` -->

<!-- ### 反馈问题（强烈建议带日志）

提 Issue 前请准备：

- **复现步骤**（做了什么、卡在哪里）
- **运行日志**：`debug/maa.log`
- **分辨率/模拟器版本/控制器类型**（ADB/Win32） -->

<!-- ## 开发者指南（贡献者）

- **框架**：本项目基于 [MaaFramework](https://github.com/MaaXYZ/MaaFramework)
- **推荐插件**：VSCode 的 [Maa Pipeline Support](https://marketplace.visualstudio.com/items?itemName=nekosu.maa-support)
- **开发规范/格式化**：见 `docs/zh_cn/个性化配置.md`（包含 prettier / markdownlint / oxipng / pre-commit） -->
<!-- 
### 资源与接口

- **项目接口定义**：`assets/interface.json`（任务入口、描述、控制器等）
- **图片资源**：`assets/resource/image/`
- **Pipeline**：`assets/resource/pipeline/`（JSON） -->

<!-- ## 即刻开始

- [📄 快速开始](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/1.1-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md)
- [🎞️ 视频教程](https://www.bilibili.com/video/BV1yr421E7MW) -->

<!-- ## 如何开发

0. 使用右上角 `Use this template` - `Create a new repository` 来基于本模板创建您自己的项目。

1. 克隆本项目（地址请修改为您基于本模板创建的新项目地址）。

    ```bash
    git clone https://github.com/MaaXYZ/MaaPracticeBoilerplate.git
    ```

2. 下载 MaaFramework 的 [Release 包](https://github.com/MaaXYZ/MaaFramework/releases)，解压到 `deps` 文件夹中。

3. 下载 OCR（文字识别）资源文件 [ppocr_v5.zip](https://download.maafw.xyz/MaaCommonAssets/OCR/ppocr_v5/ppocr_v5-zh_cn.zip) 解压到 `assets/resource/model/ocr/` 目录下，确保路径如下：

    ```tree
    assets/resource/model/ocr/
    ├── det.onnx
    ├── keys.txt
    └── rec.onnx
    ```

    _请注意，您不需要将 OCR 资源文件上传到您的代码仓库中。`.gitignore` 已经忽略了 `assets/resource/model/ocr/` 目录，且 GitHub workflow 在发布版本时会自动配置这些资源文件。_

4. 进行开发工作，按您的业务需求修改 `assets` 中的资源文件，请参考 [MaaFramework 相关文档](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/1.1-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md#%E8%B5%84%E6%BA%90%E5%87%86%E5%A4%87)。

5. 完成开发后，上传您的代码并发布版本。

    ```bash
    # 配置 git 信息（仅第一次需要，后续不用再配置）
    git config user.name "您的 GitHub 昵称"
    git config user.email "您的 GitHub 邮箱"
    
    # 提交修改
    git add .
    git commit -m "XX 新功能"
    git push origin HEAD -u
    ```

6. 发布您的版本

    需要**先**修改仓库设置 `Settings` - `Actions` - `General` - `Read and write permissions` - `Save`

    ```bash
    # CI 检测到 tag 会自动进行发版
    git tag v1.0.0
    git push origin v1.0.0
    ```

7. 更多操作，请参考 [个性化配置](./docs/zh_cn/个性化配置.md)（可选） -->

<!-- ## 生态共建

MAA 正计划建设为一类项目，而非舟的单一软件。

若您的项目依赖于 MaaFramework，我们欢迎您将它命名为 MaaXXX, MXA, MAX 等等。当然，这是许可而不是限制，您也可以自由选择其他与 MAA 无关的名字，完全取决于您自己的想法！

同时，我们也非常欢迎您提出 PR，在 [社区项目列表](https://github.com/MaaXYZ/MaaFramework#%E7%A4%BE%E5%8C%BA%E9%A1%B9%E7%9B%AE) 中添加上您的项目！

## FAQ

### 0. 我是第一次使用 git，这是什么？视频演示中那个黑框框命令行哪来的？

黑框框是 git bash，几乎任何现代软件的开发都离不开 git，建议先参考 [菜鸟教程](https://www.runoob.com/git/git-install-setup.html) 或搜索一些视频，学习完 git 后再来进行后续开发工作。

### 1. 我是第一次使用 Python，在命令行输入 `python ./configure.py` 或 `python -m pip install MaaFW` 之后没有反应？没有报错，也没有提示成功，什么都没有

Win10 或者 Win11 系统自带了一份 "Python"，但它其实只是一个安装器，是没法用的。  
你需要做的是关闭它或者删除它的环境变量，然后自己去 Python 官网下载并安装一份 Python。  
[参考方法](https://www.bilibili.com/read/cv24692025/)

### 2. 使用 MaaDebugger 或 MaaPicli 时弹窗报错，应用程序错误：应用程序无法正常启动

![缺少运行库](https://github.com/user-attachments/assets/942df84b-f47d-4bb5-98b5-ab5d44bc7c2a)

一般是电脑缺少某些运行库，请安装一下 [vc_redist](https://aka.ms/vs/17/release/vc_redist.x64.exe) 。

### 3. 我在这个仓库里提了 Issue 很久没人回复

这里是《项目模板》仓库，它仅仅是一个模板，一般很少会修改，开发者也较少关注。  
在此仓库请仅提问模板相关问题，其他问题最好前往对应的仓库提出，如果有 log，最好也带上它（`debug/maa.log` 文件）

- MaaFW 本身及 MaaPiCli 的问题：[MaaFramework/issues](https://github.com/MaaXYZ/MaaFramework/issues)
- MaaDebugger 的问题：[MaaDebugger/issues](https://github.com/MaaXYZ/MaaDebugger/issues)
- 不知道算是哪里的、其他疑问等：[讨论区](https://github.com/MaaXYZ/MaaFramework/discussions)

### 4. OCR 文字识别一直没有识别结果，报错 "Failed to load det or rec", "ocrer_ is null"

**请仔细阅读文档**，你无视了前面步骤的报错。我不想解释了，请再把本文档仔细阅读一遍！ -->
