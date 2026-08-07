---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: Biolinq ships the Shine biosensor and a companion consumer mobile app only — its entire public web presence is an 11-page Webflow marketing site whose /support page reads "Intentionally left blank", and api/developer/docs/app.biolinq.com all fail to resolve in DNS.
  evidence:
  - status: 200
    url: https://www.biolinq.com/support
  - status: 404
    url: https://www.biolinq.com/openapi.json
  - status: 404
    url: https://www.biolinq.com/.well-known/agent-card.json
  - status: 404
    url: https://www.biolinq.com/llms.txt
  - status: 0
    url: https://api.biolinq.com/
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: Biolinq Incorporated is a San Diego, California medical device and digital health company founded in 2012 that develops intradermal biowearable sensors. Its lead product, Biolinq Shine, is an autonomous needle-free continuous glucose sensor built on an array of electrochemical microsensors that sit just below the surface of the skin, combined with an accelerometer and an ambient light sensor so a single wearable measures glucose alongside activity and sleep. The sensor carries an on-body LED color indicator for time-in-range and pairs with a companion mobile application for trends and insights. The FDA granted Biolinq Shine De Novo classification for adults with type 2 diabetes not on insulin therapy, with a planned US market launch. Biolinq publishes no public developer program, API documentation, or machine-readable API contract; its public web presence is a corporate marketing site.
image: https://cdn.prod.website-files.com/6310feecd52f6e2e081df17e/633c9a9b7cdf016ec08ae0d3_biolinq-logo-white%203.png
layout: provider
modified: '2026-08-07'
name: Biolinq
nav: Providers
network: true
random_paper: 72
slug: biolinq
tags:
- Company
- Health
- Digital Health
- Medical Devices
- Wearables
- Biosensors
- Continuous Glucose Monitoring
- Diabetes
---
