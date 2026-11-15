# 内容整理报告

> 本轮只做可证实的类型分流与文案清理；不删除记录、不改许可与证据。

## 汇总

| 项 | 数量 |
| --- | --- |
| 总记录 | 1763 |
| photos | 1721 |
| paintings | 23 |
| objects | 16 |
| links | 3 |
| 待核 | 0 |

### 类型分布

| 类型 | photos | paintings | objects | links |
| --- | --- | --- | --- | --- |
| photograph | 1664 | 0 | 0 | 0 |
| postcard | 34 | 0 | 2 | 0 |
| print | 22 | 4 | 0 | 0 |
| drawing | 0 | 1 | 0 | 0 |
| object | 0 | 0 | 13 | 0 |
| painting | 0 | 18 | 0 | 0 |
| link | 0 | 0 | 0 | 3 |
| document | 1 | 0 | 1 | 0 |

## 第二轮内容收尾（2026-11-15）

- 修正 9 条明显主题误分：Face detail / Man on Horse / Man with Walking Stick / Portret van een jongeman → 面孔；Manga Valley / Landscape with Tree / View of the Acropolis → 风景。
- 处理 142 条采集时被截断的题名：111 条按源站描述补全；31 条无法补全的标 `title_truncated: true` 并加省略号。
- 0 删除记录；许可、证据、审计、图片 sha 均未改。
- 剩余 3 条类型待核不变。

## 第三轮深度收尾（2026-11-15）

- 再移入 12 件作品：9 件油画/水彩绘画、2 件版画、1 件素描；paintings 从 8 增至 20。
- 解决全部 3 条待核：Luks 确认为油画；两封 Photostat 信件确认为不同日期的两封信，不是重复；旅行者金唱片条目确认为纪实照片并补全题名。
- 题名截断清零：Cleveland 17 条、Commons 11 条、源站描述 100+ 条已补全；0 条仍标 `title_truncated`。
- 3 条外链卡的许可快照已按现有字段重建；0 条缺 `license_snapshot`。
- 当前：0 待核、0 截断、0 缺快照。

## 第四轮：主题复审与最后补扫（2026-11-15）

- 街巷主题复审修正 52 条：10 面孔、2 远方、25 战火、5 灾变、5 风景、5 劳作。
- 补扫移入 4 件：3 件油画（Žabota、Arnesen ×2）进 paintings；1 件书页绘画复制品进 objects。
- 当前：photos 1721、paintings 23、objects 16、links 3；0 待核、0 截断、0 缺快照。
- 主题复盘的完整说明见 [`TOPIC-AUDIT.md`](TOPIC-AUDIT.md)。

## 移出照片的条目

| id | 标题 | 原 collection | 新 collection | 类型 | 依据 |
| --- | --- | --- | --- | --- | --- |
| auto-06443e0e | A pictorial Isfahan rug, signed Ahmad  | photos | objects | object | 题名与描述：pictorial Isfahan rug |
| auto-256d170f | Edith White Still life with grapes 190 | photos | paintings | painting | 源站描述：oil on canvas |
| auto-26aef174 | Postcard of Izola 1900 | photos | objects | postcard | 原分类为纸品实物；源站描述为明信片 |
| auto-27bcc7d5 | Camille Pissarro, Still Life with a Co | photos | paintings | painting | 题名 Still Life；作者 Camille Pissarro 为画家；源站文件页 |
| auto-2df8ce6f | Portrait of a Boy, by George Benjamin  | photos | paintings | painting | 题名 Portrait of a Boy；作者 George Benjamin Luks 为画家；画种待核 |
| auto-4993fdb8 | Ceylon telegraph stamp halfs | photos | objects | object | 题名：Ceylon telegraph stamp |
| auto-53f822b7 | Jamaica 1900 Album, pg 14 4859928220 | photos | objects | object | 原分类 medium: 纸品实物 |
| auto-57735d10 | Jamaica 1900 Album, pg 12 4859927972 | photos | objects | object | 原分类 medium: 纸品实物 |
| auto-5aef6dca | Photostat copy of letter signed Jas. B | photos | objects | document | 题名：Photostat copy of letter signed Jas. B. Eads |
| auto-5b6c13e5 | Romania 1957 MI 1677, 1679 stamp tript | photos | objects | object | 原分类 medium: 纸品实物 |
| auto-6196c443 | (Photograph of the 100-Millionth V-Mai | photos | objects | object | 原分类 medium: 纸品实物 |
| auto-68c899de | Stereoscope, Richard Verascope, ca. 19 | photos | objects | object | 原分类 medium: 纸品实物 |
| auto-69cf0522 | 10 cents - British Ceylon - Silver (19 | photos | objects | object | 题名：10 cents - British Ceylon - Silver；按钱币/器物处理 |
| auto-9afb2e56 | Portrait of an old woman LACMA 83.1.13 | photos | paintings | print | 源站描述：Etching on wove paper |
| auto-b21888a0 | A Kashan 'Mohtasham' pictorial rug, ce | photos | objects | object | 题名与描述：Kashan pictorial rug |
| auto-ba5de885 | Jamaica 1900 Album, pg 19 4859308273 | photos | objects | object | 原分类 medium: 纸品实物 |
| auto-c6739d13 | Kirkcaldy fishing boat in harbour | photos | paintings | painting | 源站描述：Watercolour |
| auto-d49e9fd0 | Still life with orange and book-raphae | photos | paintings | painting | 题名 Still Life；作者 Raphaelle Peale 为画家；源站文件页 |
| auto-d713ad77 | Classroom 19th century English School | photos | paintings | painting | 源站描述：Oil on canvas |
| auto-dc10d302 | Photostat copy of letter signed Jas. B | photos | objects | object | 原分类 medium: 纸品实物 |
| auto-dd7aafa6 | Marius Bauer.'A Street in Cairo'.Etchi | photos | paintings | print | 源站描述：Etching on paper |
| auto-f457f794 | Postcard of Town Square in Ljubljana 1 | photos | objects | postcard | 原分类为纸品实物；源站描述为明信片 |
| auto-f49110d3 | Romania 1957 MI 1678, 1680 stamp tript | photos | objects | object | 原分类 medium: 纸品实物 |

## 待核条目

| id | 标题 | 类型 | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| auto-2df8ce6f | Portrait of a Boy, by George Benjamin  | painting | needs_review | 题名与作者指向绘画；源站未直接写出画种，标为待核。 |
| auto-5aef6dca | Photostat copy of letter signed Jas. B | document | needs_review | 与 auto-dc10d302 题名相同，待核是否重复。 |
| auto-768ea122 | Voyager-golden-record-etching-7-28-77  | photograph | needs_review | 画面主体是金唱片蚀刻细节，作为航天影像保留，类型待核。 |

## 文案清理

- 33 条无 `curation` 字段的人工精策展文案保留原文。
- 其余自动批次改为：年代 / 地点 / 作者 / 来源 / 馆藏编号 / 类型句。
- 不再沿用按 topic 生成的“短评”，避免静物、绘画、器物被写成街巷或劳作。

## 未做的事

- 没有按题名关键词批量移动；没有删除任何记录。
- 没有把明信片全部移出 photos：它们仍是以摄影为载体的影像，但 `content_type` 标为 `postcard`、`medium` 标为 `明信片`。
- 绘画/版画的画种只在源站有明确工艺词时写明；不明确的写 `绘画` 或标待核。
