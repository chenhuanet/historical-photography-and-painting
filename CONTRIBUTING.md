# 贡献指南

每一条新增素材都是一次**人工权利核验**。请把它当成一次档案登记，而不是往图库里传图。

## 一条内容由两个文件组成

- `content/photos/<id>.json` —— 结构化元数据、许可档位与权利快照
- `content/notes/<id>.md` —— 你写的策展叙事（纯文本一段，不要加标题和 Markdown 标记，`build.py` 会原样注入卡片）

`<id>` 用小写字母、数字与连字符，例如 `1936-migrant-mother`。两个文件名必须一致，且 `id` 字段也要一致。

只做外链、不落地图片的 L3/L4 源，放 `content/links/<id>.json`，同样配一份 `notes`。

## 新增一张图的步骤

1. 确认许可：到**源站文件页**核对，不要只信搜索结果或机构级声明。记录许可证全文链接、作者、原始著录、抓取时间。
2. 判定档位：`L0` CC0 / 公有领域 / 政府作品；`L1` CC BY / PDM；`L2` CC BY-SA；`L3` CC BY-NC*；`L4` 权利保留或未评估。
3. **只有 L0 / L1 / L2 能进 `content/photos/`**。L3 只能做外链卡，L4 只能做外链卡且必须确认源站不禁止链接。
4. 复制一条现有 json 作模板，补齐字段；`image` 填源站展示尺寸 URL，`local_image` 填 `assets/img/<id>.jpg`（或 `.png`）。**不要把图片二进制提交进仓库。**
5. 按 [`schema/taxonomy.json`](schema/taxonomy.json) 填满五维分类：`kind` / `theme` + `topic` / `region` / `medium` / `period`。大类与细类必须匹配（例如「人间」只能配面孔、街巷、劳作）。
6. 填 `evidence`：一句能对照源站核验的核心史实陈述、依据类型、馆藏编号、源文件页链接、核验日期、状态。**这是台账的来源，不能留空，也不要写推测。** 事实以源站著录为准。
7. 写 `content/notes/<id>.md`，一段话说明这张图记录了什么、为什么值得收。可以生动，但不能编造人物身份、心理或未见于著录的情节。
8. 本地跑通：
   ```
   python scripts/fetch_images.py
   python scripts/validate.py
   python scripts/build.py
   ```
   构建会顺带刷新站点台账与 `PROVENANCE.md`，不用手改。
9. 提 PR，并在描述里贴出源站文件页链接与许可截图/引用。

## 会被 CI 挡掉的情况

`scripts/validate.py` 是硬卡口，以下任一情形都会拒绝构建：

- 缺必填字段、`id` 与文件名不一致或重复；
- 许可命中黑名单（NC / ND / 权利保留 / 未评估）却放在 `photos/`；
- `tier` 为 L3/L4 却带 `image` 或 `local_image`；
- 缺策展笔记、链接不是合法 http(s)、缺抓取时间快照；
- 五维分类缺项、值不在词表内、`theme` 与 `topic` 错配、`period` 格式不对；
- `evidence` 台账缺字段、源文件页不是合法链接、核验日期格式不对；
- 缺 `audit` 字段、`human_review` 不是 `false`、`run_id` 无法关联到 `logs/` 里的运行记录；
- 事件文件中混入政治、选举、战争、人物争议类待复核文本。

本站**没有人工审核**，但也不是「随便收」。下列三个脚本是一条批次流程（新增批次时要同步更新 `curate.py` 的策展表），每一步都要保留日志：

```
python scripts/ingest.py    # 严谨采集，逐条写 logs/ingest.jsonl
python scripts/review.py    # 独立复核，逐条写 logs/review.jsonl
python scripts/curate.py    # 策展放行，逐条写 logs/curate.jsonl
python scripts/build.py     # 刷新 AUDIT.md 与站点台账
```

修改任何门槛或规则时，请同时更新 `audit.py` 里的 `RULES_VERSION`，让台账能区分「按哪一版规则判的」。不要把 `needs_review` 的条目直接搬进 `content/`——那等于绕过复核。

规则本身在 `schema/photo.schema.json`，改规则请连 `validate.py` 一起改，并在 PR 里说明理由。

## 内容审核

历史影像涉及战争、灾难、可识别人物与隐私时，描述保持克制、就史料论史料，不作评判、不作戏剧化渲染。当代政治、选举、人物争议类**事件文本**不进公开仓：采集器会把它放进人工复核队列，只记录数量。涉敏素材先放私有待核验区，确认无异议后再提升。

## DCO

提交需签署开发者原创声明，用带签名的 commit：

```
git commit -s -m "add: 1936 migrant mother"
```

这表示你确认所提交的内容由你创作，或你有权按本仓库的许可条款贡献它；**图片本体不适用此声明**，其权利仍归原权利人。

## 审核标准

维护者会看：许可证据是否充分、出处是否可点开核验、日期与地点是否有依据、`evidence` 的史实陈述能否在源站逐字对上、五维分类是否贴切、策展文字是否生动但克制、是否引入了新的权利风险。宁可少收一张，不可错收一张。
