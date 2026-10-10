# 《草莓奶油蛋糕》多参考绑定说明

针对官方工作流「MiniMax H3官方工作流_多参考生成视频」（6 参考槽）。

## 方案 A：单参考（最稳，已验证 16 部）
- 槽1 = 芙宁娜角色卡（`furina_single.png`，单视图！）
- 提示词已按此写好：`<Picture 1>` 只在 `subject_definitions` 里引用
- 直接粘贴 `cake_fastcut.txt`，无需改动

## 方案 B：双参考（加蛋糕产品锚点）
- 槽1 = 角色卡；槽2 = **成品蛋糕参考图**
- 提示词需补两处（否则 `<Picture 2>` 悬空引用会困惑模型）：

1）`subject_definitions` 里 `<Subject 2>` 末尾追加：
```
The finished cream cake in this video is exactly the cake shown in <Picture 2>, whose design and proportions are reproduced faithfully.
```
2）`retention_analysis` 的 `<Subject 2>` 行末尾追加：
```
, and the finished cream cake matches <Picture 2> in every shot where it appears
```

## 方案 C：三参考（加厨房场景图）
- 槽1 = 角色；槽2 = 蛋糕；槽3 = 厨房场景
- 同样把 `<Picture 3>` 引用补进 `<Subject 2>` 定义（场景图只定义环境，**不单独建 Picture 条目**）

## 硬规则（必守）
| 规则 | 原因 |
|---|---|
| 参考图**必须单视图** | 三视图拼图 → 成片出现角色副本，实测声明无效 |
| 参考图**图内零文字** | 标注/水印会被模型当成画面内容印进成片 |
| 角色卡**只传一张** | 传 2 张参考图的开销超过画面本身 |
| 多角度**不拼成一张** | 确需多角度时分放不同槽位 |

## 渲染档位建议
- `Lite/Standard` 或 `Lite/Plus`：快速验证构图与切点
- `Ultra（60000）`：成片档，20 步，脸部与音乐最稳
