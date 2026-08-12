---
api_count: 1
artifact_total: 0
coverage:
  checked: '2026-08-11'
  detail: CounterTack now trades as GoSecure, and its live Titan API host api.gosecure.net returns HTTP 401 on every path probed — including /robots.txt and every /.well-known/ path — while the Titan console sits behind a Keycloak tenant login, so the contract and reference are reachable only by an existing GoSecure customer.
  evidence:
  - status: 401
    url: https://api.gosecure.net/openapi.json
  - status: 401
    url: https://api.gosecure.net/robots.txt
  - status: 200
    url: https://titan.gosecure.net/
  - status: 200
    url: https://www.gosecure.ai/sitemap.xml
  - status: 0
    url: https://countertack.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-11'
description: 'CounterTack, Inc. was a Waltham, Massachusetts endpoint detection and response (EDR) vendor whose Sentinel and Endpoint Threat Platform products applied behavioral analysis, memory forensics and machine learning to detect zero-days, rootkits and advanced persistent threats. In June 2018 CounterTack acquired its channel partner GoSecure, a managed detection and response (MDR) provider, and in March 2019 rebranded the combined company as "GoSecure powered by CounterTack"; the CounterTack name has since been retired in favour of GoSecure, which today markets a managed extended detection and response (MXDR) service and the GoSecure Titan platform covering EDR, IDR, NGAV, SIEM and professional services. The CounterTack surface is therefore historical: countertack.com still resolves to GoSecure infrastructure but serves no valid certificate, and the living platform is customer-only behind a Keycloak single sign-on at titan.gosecure.net.'
image: https://www.gosecure.ai/images/sharing/gosecure-facebook.jpg
layout: provider
modified: '2026-08-11'
name: CounterTack
nav: Providers
network: true
random_paper: 27
slug: countertack
tags:
- Company
- Security
- Cybersecurity
- Endpoint Security
- Endpoint Detection and Response
- Managed Detection and Response
- Threat Detection
- Incident Response
- SIEM
---
