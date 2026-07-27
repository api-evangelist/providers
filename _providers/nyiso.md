---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Free - Open bulk data; REST APIs restricted to market participants
  method: observed
  onboarding: open
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
api_count: 6
artifact_total: 0
created: '2026-07-27'
description: The New York Independent System Operator (NYISO) is the not-for-profit FERC-jurisdictional entity that operates New York State's bulk electricity grid, administers the state's wholesale energy, capacity and ancillary-services markets, and performs long-term power system planning. Formed in 1999 out of the New York Power Pool, it sits squarely in the wholesale middle of the value chain - between generators, transmission owners and interconnectors on one side and the investor-owned utilities and retail suppliers who actually bill New York consumers on the other. NYISO's API posture is the sector's classic two-speed split, and NYISO lands hard on both ends of it. Market and system data is genuinely open - the MIS public archive at mis.nyiso.com/public serves roughly sixty machine-readable report families (day-ahead and real-time LBMP, actual and forecast load, real-time fuel mix, ATC/TTC, outages, constraints, interface flows, bid data, capacity, uplift, emissions) as daily CSV
  and monthly ZIP with no account, no key and no referrer check, and the FERC-mandated OASIS node publishes an anonymously listable object store of transmission postings. Consumer data is the exact opposite - there is none, and none is expected, because NYISO holds no retail customer relationships. Every real REST API NYISO documents - the Finance APIs (Metering, Settlements, Invoicing) and the Metering API under api.nyiso.com - is market-participant-only, gated behind an MIS user account plus a NAESB-accredited digital certificate, and every one of those endpoints answers 401 anonymously. The United States has no consumer energy data mandate behind Green Button, and in any case Green Button binds distribution utilities, not system operators, so NYISO carries no Green Button or Consumer Data Right obligation at all.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: New York Independent System Operator (NYISO)
nav: Providers
network: true
random_paper: 18
slug: nyiso
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- Open Data
- System Operator
- New York
- Renewables
- Emissions
---
