# -*- coding: utf-8 -*-
"""Klook 合作方开放平台客户端（v3）。"""
import hashlib
import hmac
import time
import urllib.parse

BASE_URL = "https://api.klook.com/v3"
SANDBOX_URL = "https://sandbox-api.klook.com/v3"


class KlookPartnerClient:
    def __init__(self, supplier_id, secret="", sandbox=False):
        self.supplier_id = supplier_id
        self.secret = secret
        self.base = SANDBOX_URL if sandbox else BASE_URL

    def _headers(self, path):
        ts = str(int(time.time()))
        raw = "%s|%s|%s" % (self.supplier_id, path, ts)
        sig = hmac.new(self.secret.encode(), raw.encode(), hashlib.sha256).hexdigest()
        return {"X-Klook-Supplier": self.supplier_id, "X-Klook-Ts": ts, "X-Klook-Sign": sig}

    def activities(self, city):
        path = "/activities?" + urllib.parse.urlencode({"city": city, "page_size": 50})
        return self.base + path, self._headers(path)


if __name__ == "__main__":
    print(KlookPartnerClient("klk_supplier_2041").activities("bangkok")[0])
