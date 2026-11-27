# 专题

专题是“精选 + 论点”的策展层，不是标签页。每个专题一个 Markdown 文件。

```yaml
---
id: first-fifty-years
collection: photos
title: 摄影术的前五十年
subtitle: 从银版到快照，光如何学会留下细节
status: published
cover: 1843-daguerreotype
themes: [技艺]
chapters:
  - title: 先让脸留下来
    text: 这一章要回答的问题。
    items:
      - id: 1843-daguerreotype
        caption: 图注：看到什么、为什么在这里、来源。
---

导语写在 frontmatter 之后，用 2–3 段说明专题的论点。
```

规则：

- `cover` 必须在 `chapters[].items` 里。
- `item.id` 必须存在于对应 collection。
- 一张图可以出现在多个专题；照片记录不写 `stories` 字段。
- 专题页是精选，集合页是全量，两者不混。

当前：主站发布 **380** 篇故事，另有 **4** 篇归档在 `_archive/`；366 天日历全覆盖。主题轴与编辑串读见 [`../story-axes.json`](../story-axes.json) 与 [`../story-trails.json`](../story-trails.json)。

代表性长文：

- [摄影术的前五十年](photos/first-fifty-years.md)
- [没有留下名字的人](photos/unnamed-faces.md)
- [从地球到月面](photos/earth-to-moon.md)
- [街角的一天](photos/street-a-day.md)
- [手上的工作](photos/hands-at-work.md)
- [中国，1850–1930](photos/china-1850-1930.md)
