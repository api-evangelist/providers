---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Paid · Contract required for organisational access; free self-serve for your own meter data via Bright
  method: manual
  onboarding: request
  pricing: paid
  public: false
  source:
  - https://data.glowforindustry.com/
  - https://docs.glowmarkt.com/GlowmarktAPIDataRetrievalDocumentationIndividualUserForBright.pdf
  trial: false
  try_now: false
api_count: 5
artifact_total: 0
created: '2026-07-27'
description: 'Hildebrand Technology Limited is a London-based energy data company and, since 2019, the United Kingdom''s first independent DCC Other User with a direct connection to the Smart Data Communications Company network. It sits between Britain''s mandated smart-metering infrastructure and the applications built on top of it: it makes Glow hardware (CADs, in-home displays, sub-meters, temperature sensors), ingests and stores smart-meter reads at scale, and republishes them through the Glowmarkt Platform APIs, the consumer Bright app, and the commercial Glow Data Service. Its API posture is an honest reflection of the British market seam — Britain mandated the metering INFRASTRUCTURE, not a consumer data right, so there is no Consumer Data Right or Green Button obligation on Hildebrand and no standards-conformant data-sharing surface to point at. What exists instead is a proprietary but genuinely well-documented platform: five public Swagger 2.0 definitions are served anonymously
  from api.glowmarkt.com/api-docs, and any individual who installs Bright, creates an account and passes meter-point verification can call the same production API for their own household data with a published applicationId. Third-party organisational access to other people''s data is the closed half — it runs through Glow Data Service on a signed contract from GBP 595/month per MPxN, with consumer verification and consent captured per meter point. Hildebrand publishes no open grid or market data of any kind: every documented endpoint returns HTTP 400 without an applicationId header, so this is a closed-market-data, consent-gated-consumer-data provider.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: Hildebrand
nav: Providers
network: true
random_paper: 17
slug: hildebrand
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Data
- Demand Response
- IoT
- Metering
---
