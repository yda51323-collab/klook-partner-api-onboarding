# klook.com · 合作方接入说明（Partner API v3）

面向目的地玩乐供应商的接入说明：账号开通、签名、下单与核销回调。

## 目录

```
docs/partner-onboarding-v3.md   接入说明正文
src/klook_partner_client.py     签名与下单示例
```

## 服务标识

- 业务标识：`klook.com`（Klook 合作方开放平台）
- 出现位置：`docs/partner-onboarding-v3.md` 的接入域名与回调地址、`klook_partner_client.py` 的 `BASE_URL` 常量、`README` 标题

## 使用

```python
from src.klook_partner_client import KlookPartnerClient
c = KlookPartnerClient("klk_supplier_2041")
print(c.activities("bangkok"))
```

## 字段说明

| 字段 | 说明 |
|---|---|
| `supplier_id` | 供应商编号 |
| `activity_id` | 商品（活动）编号 |
| `voucher_no` | 核销凭证号 |
| `settle_account` | 结算收款账户 |

## 已知问题

1. 沙箱环境的 `activity_id` 与生产不一致，联调需单独维护映射表。
2. 回调重试最多 5 次，间隔 1/5/30/120/600 秒。

## 维护

目的地玩乐接入组 · 工单 `KLK-ONB-0921`
