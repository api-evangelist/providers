---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Free · Anonymous undocumented data feeds · No developer program
  method: manual
  onboarding: none-published
  pricing: free
  public: true
  source:
  - documentation
  - probes
  trial: false
  try_now: true
api_count: 4
artifact_total: 0
created: '2026-07-27'
description: 'SaskPower — the Saskatchewan Power Corporation — is the Crown corporation that owns and runs essentially the whole electricity value chain in the province of Saskatchewan, Canada. Established in 1929 as the Saskatchewan Power Commission and continued as the Saskatchewan Power Corporation in 1949 under The Power Corporation Act, it is owned by the provincial government through Crown Investments Corporation and reports to a Minister Responsible rather than to shareholders. It generates, transmits, distributes and retails power to more than 550,000 customers across roughly 652,000 square kilometres on more than 160,000 kilometres of line, from a fleet of coal, natural gas, hydro, wind and solar facilities totalling about 5,437 MW. Unlike Ontario or Alberta there is no competitive wholesale market operator sitting beside it — SaskPower is generator, wires company and retailer at once. Its API posture is the exact inverse of a regulated open-banking-style utility: no consumer energy
  data mandate applies to it at all. Saskatchewan has no Green Button regulation (Ontario and Nova Scotia do), Canada has no national energy consumer data right, and the Green Button Alliance states plainly that it has no information about any Green Button deployment in Saskatchewan. Smart meter usage data is visible only to the account holder inside MySaskPower behind an Azure AD B2C login; there is no consented third-party data-sharing API, no ESPI/Green Button surface, and no accreditation scheme. What SaskPower does publish — and publishes wide open, anonymously, with no key, no signup and no rate limit — is grid and system data: a live JSON feed of provincial system demand, generation by fuel type, net interchange and historical peak demand behind the public "Where Your Power Comes From" page, an RSS feed of planned outages, and two KML feeds driving the outage and smart-meter installation maps. None of it is documented as an API, versioned, or covered by a developer program: the former
  SaskPower ESB developer portal at api-info.saskpower.com no longer resolves, and api.saskpower.com is a live TIBCO/Mashery gateway that answers every public path with ERR_596_SERVICE_NOT_FOUND. Open market data, closed consumer data, and no published door for a developer to knock on.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: SaskPower
nav: Providers
network: true
random_paper: 39
slug: saskpower
tags:
- Energy
- Canada
- Utilities
- Electricity
- Grid
- Smart Metering
- Crown Corporation
- Outages
- Renewables
- Open Data
---
