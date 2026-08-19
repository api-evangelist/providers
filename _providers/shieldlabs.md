---
api_count: 1
artifact_total: 0
created: '2026-08-19'
description: 'Anonymous visitor identification and fraud-prevention platform. A browser ES-module snippet loaded from cdn.shieldlabs.ai collects 100+ device and network signals and returns six persistent identifiers (DeviceID, VisitorID, CookieID, SessionID, RequestID and a caller-supplied hashed UserHID) plus an explainable 0-100 Risk Score built from weighted anonymity signals — VPN, proxy, Tor, privacy relay, datacenter, IP reputation, anti-detect browser, geolocation spoofing, OS mismatch, incognito, browser automation and suspicious paid clicks. ShieldLabs deliberately makes no allow/challenge/block decision: it returns the score and the signals behind it, and the customer''s own code owns the verdict. Delivery is a signed at-most-once webhook (identification.scored, HMAC-SHA256 in X-Shield-Signature, no retries), backed by two server-side REST surfaces — a free History API on account.shieldlabs.ai and a billed Management API on api.shieldlabs.ai — described by a public OpenAPI 3.1
  specification the company maintains in its own MIT-licensed GitHub repo. Self-serve and per-identification priced, with a 5,000-identification free tier and no sales gate.'
image: https://shieldlabs.ai/og/home.png
layout: provider
modified: '2026-08-19'
name: ShieldLabs
nav: Providers
network: true
random_paper: 8
slug: shieldlabs
tags:
- fraud-detection
- abuse-prevention
- visitor-identification
- device-fingerprinting
- bot-detection
- vpn-proxy-detection
- risk-scoring
- identity
- security
- webhooks
- anti-fraud
- traffic-quality
---
