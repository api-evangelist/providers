---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affy-medtech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affymedtech.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/affy-medtech-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/affy-medtech-llms.txt
coverage:
  checked: '2026-09-02'
  detail: affymedtech.com serves a 1,235-byte "Coming Soon" placeholder and returns a real 404 on every other path including /docs, /openapi.json and all eight probed /.well-known/ documents, while api., docs., developer. and portal. subdomains of affymedtech.com do not resolve in DNS at all — the Lynx platform is sold and deployed as an enterprise hospital system with no public developer program of any kind.
  evidence:
  - status: 200
    url: https://affymedtech.com/
  - status: 404
    url: https://affymedtech.com/openapi.json
  - status: 404
    url: https://affymedtech.com/docs
  - status: 404
    url: https://affymedtech.com/.well-known/agent-card.json
  - status: 404
    url: https://affymedtech.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: Affy MedTech is a UK- and Netherlands-based health technology company behind Lynx, a modular, cloud-hosted platform for hospitals and healthcare delivery organisations that consolidates authoritative treatment information, patient booking, electronic medical records, clinical documentation, billing and claims validation, reporting, remote diagnostics and ambulatory ECG into a single system. Its Patient Interaction Module gives patients access to their own records, prescriptions, diagnostic images and treatment plans with self-service booking, digital consent and online payment, while the Super Switch Module acts as a real-time integration bridge between hospital systems such as radiology, laboratory and billing. The platform is marketed alongside Total Doctor / Total Health and is deployed by international hospital groups as well as smaller clinics and specialist centres. Affy MedTech is a Silver Industry Partner of openEHR International and operates alongside Vertice Software
  Solutions, which publishes Lynx in other markets. AFFY MEDTECH UKI LTD (company number 17000777) was incorporated in England on 30 January 2026 and is controlled by Affy Medtech B.V. of Amsterdam. As of September 2026 affymedtech.com serves only a "Coming Soon" placeholder and the company publishes no public developer program, API reference or machine-readable contract.
image: https://openehr.org/wp-content/uploads/2026/05/300x300-17.png
layout: provider
modified: '2026-09-02'
name: Affy MedTech
nav: Providers
network: true
overview: Affy MedTech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Health IT, Electronic Health Records, and openEHR.
plans:
- name: Affy Medtech Plans Pricing
  plan_count: 0
  slug: affy-medtech-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Affy Medtech Rate Limits
  slug: affy-medtech-rate-limits
security:
- kind: domain-security
  name: Affy Medtech Domain Security
  slug: affy-medtech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affy-medtech
tags:
- Company
- Health Care
- Health IT
- Electronic Health Records
- openEHR
- Hospital Management
- Medical Records
- Interoperability
- Remote Diagnostics
- United Kingdom
website: https://affymedtech.com/
---
