---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: Bluewhite advertises a "Software SDK" and an "API platform" on its technology page but publishes no reference behind them — the only route is the contact form, and the Compass operator platform 302s every path, including /openapi.json, to a Keycloak OIDC login.
  evidence:
  - status: 200
    url: https://www.bluewhite.ai/technology
  - status: 302
    url: https://compass.bluewhite.ai/openapi.json
  - status: 503
    url: https://auth.bluewhite.ai/realms/maia-cloud/.well-known/openid-configuration
  - status: 404
    url: https://www.bluewhite.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.bluewhite.ai/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-07'
description: 'Blue White Robotics Ltd. — operating as Bluewhite — is an Israeli off-road autonomy company founded in 2017 by Ben Alfi, Yair Shahar and Aviram Shmueli, headquartered in Tel Aviv with a US operation in Fresno, California. Bluewhite builds an OEM-agnostic autonomy stack that retrofits conventional vehicles into unmanned ground vehicles: Pathfinder, an aftermarket autonomy kit combining control, intelligence and perception modules over a distributed CAN network, and Compass, a cloud fleet-operations SaaS that lets operators remotely supervise, task and monitor an autonomous fleet. The company began in permanent-crop agriculture — autonomous spraying, mowing and harvest support across roughly 150,000 US acres for 20-plus growers — and has since extended the same GPS-denied navigation and perception stack to defense and homeland-security ground robotics. Elbit Systems'' FUSE acquired 100% of Blue White Robotics in 2026. Bluewhite markets a Software SDK and an "API platform" for
  OEM and system integration, but publishes no public developer portal, API reference, or machine-readable specification; the Compass operator platform sits behind a Keycloak/OIDC login and integration access runs through a contact-sales form.'
image: https://cdn.prod.website-files.com/63bbd401d9936c49d2edf55f/686fed1ea1aabd319517cf1b_BLUEWHITE-LOGO-HORIZONTAL-FULL_COLOR.png
layout: provider
modified: '2026-08-07'
name: Blue White Robotics
nav: Providers
network: true
random_paper: 7
slug: blue-white-robotics
tags:
- Company
- Robotics
- Autonomous Vehicles
- Agriculture
- Agricultural Technology
- Artificial Intelligence
- Fleet Management
- Defense
- Unmanned Ground Vehicles
- Israel
---
