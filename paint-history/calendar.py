# -*- coding: utf-8 -*-
"""366 个“今日一画”编辑槽位。

这不是创作日期，也不是历史事件日期；它是编辑排期：
每天一件绘画，让 101 件绘画在一年内被重新看见。
"""
from datetime import date, timedelta

MONTH_ZH = ["一月", "二月", "三月", "四月", "五月", "六月",
            "七月", "八月", "九月", "十月", "十一月", "十二月"]
MONTH_EN = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]

# 艺术史上的今天：只收有确切日期的生卒、开幕与完成记录。
# 不做“每日一条”的填充；没有确切日期的事件不进入这张表。
ART_EVENTS = [
    {"date": "01-19", "year": 1839, "zh": "塞尚生于普罗旺斯艾克斯", "en": "Cézanne born in Aix-en-Provence"},
    {"date": "01-23", "year": 1832, "zh": "马奈生于巴黎", "en": "Manet born in Paris"},
    {"date": "01-23", "year": 1944, "zh": "蒙克卒于奥斯陆近郊", "en": "Munch dies near Oslo"},
    {"date": "02-06", "year": 1918, "zh": "克里姆特卒于维也纳", "en": "Klimt dies in Vienna"},
    {"date": "02-12", "year": 1942, "zh": "格兰特·伍德卒于艾奥瓦城", "en": "Grant Wood dies in Iowa City"},
    {"date": "02-13", "year": 1891, "zh": "格兰特·伍德生于艾奥瓦州阿纳莫萨", "en": "Grant Wood born in Anamosa, Iowa"},
    {"date": "02-17", "year": 1913, "zh": "军械库展览在纽约开幕", "en": "The Armory Show opens in New York"},
    {"date": "02-18", "year": 1564, "zh": "米开朗基罗卒于罗马", "en": "Michelangelo dies in Rome"},
    {"date": "02-23", "year": 1878, "zh": "马列维奇生于基辅", "en": "Malevich born in Kyiv"},
    {"date": "03-06", "year": 1475, "zh": "米开朗基罗生于卡普雷塞", "en": "Michelangelo born in Caprese"},
    {"date": "03-07", "year": 1872, "zh": "蒙德里安生于阿默斯福特", "en": "Mondrian born in Amersfoort"},
    {"date": "03-23", "year": 1887, "zh": "胡安·格里斯生于马德里", "en": "Juan Gris born in Madrid"},
    {"date": "03-30", "year": 1746, "zh": "戈雅生于丰德托多斯", "en": "Goya born in Fuendetodos"},
    {"date": "03-30", "year": 1853, "zh": "梵高生于津德尔特", "en": "Van Gogh born in Zundert"},
    {"date": "04-06", "year": 1483, "zh": "拉斐尔生于乌尔比诺", "en": "Raphael born in Urbino"},
    {"date": "04-06", "year": 1520, "zh": "拉斐尔卒于罗马", "en": "Raphael dies in Rome"},
    {"date": "04-15", "year": 1452, "zh": "达·芬奇生于芬奇", "en": "Leonardo born in Vinci"},
    {"date": "04-15", "year": 1874, "zh": "第一届印象派展览在巴黎开幕", "en": "The First Impressionist Exhibition opens in Paris"},
    {"date": "04-16", "year": 1828, "zh": "戈雅卒于波尔多", "en": "Goya dies in Bordeaux"},
    {"date": "04-30", "year": 1883, "zh": "马奈卒于巴黎", "en": "Manet dies in Paris"},
    {"date": "05-02", "year": 1519, "zh": "达·芬奇卒于昂布瓦斯", "en": "Leonardo dies at Amboise"},
    {"date": "05-06", "year": 1432, "zh": "根特祭坛画完成（扬·凡·艾克）", "en": "The Ghent Altarpiece is completed by Jan van Eyck"},
    {"date": "05-10", "year": 1849, "zh": "葛饰北斋卒于江户", "en": "Hokusai dies in Edo"},
    {"date": "05-15", "year": 1863, "zh": "落选者沙龙在巴黎开幕", "en": "The Salon des Refusés opens in Paris"},
    {"date": "05-15", "year": 1935, "zh": "马列维奇卒于列宁格勒", "en": "Malevich dies in Leningrad"},
    {"date": "05-21", "year": 1471, "zh": "丢勒生于纽伦堡", "en": "Dürer born in Nuremberg"},
    {"date": "06-07", "year": 1848, "zh": "高更生于巴黎", "en": "Gauguin born in Paris"},
    {"date": "07-15", "year": 1606, "zh": "伦勃朗生于莱顿", "en": "Rembrandt born in Leiden"},
    {"date": "07-29", "year": 1890, "zh": "梵高卒于奥维尔", "en": "Van Gogh dies in Auvers-sur-Oise"},
    {"date": "08-27", "year": 1576, "zh": "提香卒于威尼斯", "en": "Titian dies in Venice"},
    {"date": "10-04", "year": 1669, "zh": "伦勃朗卒于阿姆斯特丹", "en": "Rembrandt dies in Amsterdam"},
    {"date": "10-22", "year": 1906, "zh": "塞尚卒于普罗旺斯艾克斯", "en": "Cézanne dies in Aix-en-Provence"},
    {"date": "10-31", "year": 1632, "zh": "维米尔在代尔夫特受洗", "en": "Vermeer is baptized in Delft"},
    {"date": "10-31", "year": 1760, "zh": "葛饰北斋生于江户（传统著录）", "en": "Hokusai born in Edo (traditional date)"},
    {"date": "11-07", "year": 1929, "zh": "纽约现代艺术博物馆（MoMA）开馆", "en": "The Museum of Modern Art opens in New York"},
    {"date": "12-05", "year": 1926, "zh": "莫奈卒于吉维尼", "en": "Monet dies in Giverny"},
    {"date": "12-12", "year": 1863, "zh": "蒙克生于勒滕", "en": "Munch born in Løten"},
    {"date": "12-13", "year": 1944, "zh": "康定斯基卒于讷伊", "en": "Kandinsky dies in Neuilly-sur-Seine"},
    {"date": "12-15", "year": 1675, "zh": "维米尔卒于代尔夫特", "en": "Vermeer dies in Delft"},
    {"date": "12-16", "year": 1866, "zh": "康定斯基生于莫斯科", "en": "Kandinsky born in Moscow"},
]


def year_dates():
    """2024 is a leap year, so the calendar has 366 slots."""
    d = date(2024, 1, 1)
    out = []
    while d.year == 2024:
        out.append(d.strftime("%m-%d"))
        d += timedelta(days=1)
    return out


def build_slots(work_ids):
    """Deterministic rotation.

    101 paintings across 366 days: 63 works appear four times, 38 three times.
    Step 37 is coprime with 101, so each full cycle visits every work once.
    """
    ids = list(work_ids)
    if not ids:
        return []
    n = len(ids)
    return [{"date": md, "work": ids[(i * 37) % n]}
            for i, md in enumerate(year_dates())]


def month_of(md):
    return int(md[:2])


def day_of(md):
    return int(md[3:])


def month_days(m):
    if m == 2:
        return 29
    if m in (4, 6, 9, 11):
        return 30
    return 31


def calendar_months(slots):
    by_month = {}
    for s in slots:
        by_month.setdefault(month_of(s["date"]), []).append(s)
    return by_month
