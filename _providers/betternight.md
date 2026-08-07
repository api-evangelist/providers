---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: BetterNight is a virtual-care sleep clinic and DME operator whose only software surfaces are two robots-disallowed single-page login apps (sleep. and admin. betternight.com) that answer HTTP 200 with the identical 63KB HTML shell for every path including /openapi.json and /.well-known/agent-card.json; the marketing site is Squarespace with no /developers, /api, or docs subdomain in DNS.
  evidence:
  - status: 404
    url: https://betternight.com/developers
  - status: 404
    url: https://betternight.com/api
  - status: 404
    url: https://betternight.com/llms.txt
  - status: 404
    url: https://betternight.com/.well-known/agent-card.json
  - status: 200
    url: https://sleep.betternight.com/openapi.json
  - status: 200
    url: https://sleep.betternight.com/robots.txt
  - status: 200
    url: https://admin.betternight.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'BetterNight is a San Diego, California virtual-care sleep health company that diagnoses and treats obstructive sleep apnea end to end: telemedicine consults with sleep physicians, home sleep testing devices shipped to the patient, board-certified interpretation and therapy recommendation, home delivery of PAP and oral appliance therapy, and ongoing coaching by sleep specialists and respiratory therapists. It also offers a cognitive behavioral therapy program for insomnia and remote patient monitoring of PAP adherence. The company sells to individuals as well as to physicians, cardiologists, ENT practices, clinics, health plans and ACOs, employers, and DOT/commercial transportation programs. It reports roughly 300 sleep health professionals, Joint Commission accreditation held for over 15 years, and SOC 2 Type II compliance, and in 2026 acquired Coastal Sleep Diagnostics and Epoch Sleep Centers. BetterNight is a healthcare services operator, not an API platform: it publishes
  no developer program, API documentation, or machine-readable specification.'
image: https://static1.squarespace.com/static/5de55dfd24b1dd71d89c17f4/t/646ba565a803c661e2f30a09/1684776297362/BN_Social-Preview_2023.jpg?format=1500w
layout: provider
modified: '2026-08-07'
name: BetterNight
nav: Providers
network: true
random_paper: 54
slug: betternight
tags:
- Company
- Health
- Digital Health
- Telehealth
- Sleep Health
- Sleep Apnea
- Remote Patient Monitoring
- Medical Devices
- Virtual Care
---
