---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://amplify.asce.org/'', ''status'': 302, ''note'': ''declared website redirects to https://idp.sams-sigma.com/authorize?client_id=ASCE&response_type=code&scope=openid%2Bprofile%2Bemail%2Blicense%2Bprofile_extended%2Boffline_access&redirect_uri=https%3A//amplify.asce.org/openid-connect/sams-sigma&auth_token=eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJlbmMiOiJBMTI4R0NNIn0.Dt8ycQ8ri4c4NqsHac831uiw1tZYvKtHlVoSLOVtX86qJ1ZmmJy1B70AK-b4xnBlDAV3BimhIYkOMeDXY8jEfus3rMYDriDtV_ZlyvIXpsUa4K08mkVJVcWrb9qFYUp8u-PqYIaHfIJoopByDEEg5bpbGAXOUJy5cdzW219i9wYthOlkRA5S5d9boU4Fl5msqsLi3JSUwgte1PdKAzgmJDaSbsB-u3AI1eEzdsk0b6pAVgyKBgvQyRjwwAcJmjqHK-o-9KU930THbpMmrAc73xEIZkW5FXRwU3MUkv5jTiKwl5dwGLfuutbcjuFeSCFTVZjd6vEnujuLl06a04EThw._90E37JZ3GbJsves.ONYVg_sogJsLmlYA3ylW-q14U5ZtlM9iK7YVgL3nJ8rf5rHdJ6Uzbl5fXEU8KqSsAYHQVp6-er-KJlb0GMrIvY_S3WvteoeAr1w9ENdOgIEw86FhBv6k5Esv5aTSgxxTC_4H7VR4sUBzf_Nt0ZCr74Va3urUYUn-xZXl7nNUyebhFzOqrhNmqyd6T_cbix93RX_08a5VP5kAVA.3la3dUfVSZi3vFhnqQeWpA&ip_address=2600%3A4040%3A9270%3Ac700%3Af5db%3Ae0be%3A34ee%3A3beb&referrer_url&prompt=none&openid_connect_destination=/%3Fimplicit-login%3Dtrue&state=%257B%2522token%2522%253A%25220HgmY4HObONCcrndKH6SvPdkC0f4JHgaCTZRt9-IrSM%2522%252C%2522destination%2522%253A%2522%255C%252F%253Fimplicit-login%253Dtrue%2522%257D&shibboleth_dest=https%3A//amplify.asce.org/openid-connect/sams-sigma/login-redirect&shibboleth=true
    — a different registrable domain (asce.org -> sams-sigma.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The ASCE Hazard Tool API provides a simple interface to query locations in the United States for environmental hazard data by geographic location. It provides site-specific hazard values used in struc
  name: ASCE Hazard Tool API
  slug: hazard-tool-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asce-amplify-domain-security.yml
- group: start
  title: ASCE Amplify Platform
  type: Portal
  url: https://amplify.asce.org/
- group: start
  title: ASCE Website
  type: Portal
  url: https://www.asce.org/
created: '2025-02-17'
description: ASCE Amplify is a platform created by the American Society of Civil Engineers (ASCE) that provides civil engineering data and advocacy tools. The platform includes the ASCE Hazard Tool API, which provides a simple interface to query locations in the United States for environmental hazard data by geographic location. The Hazard Tool API covers seismic, wind, snow, ice, flood, and other environmental hazard loads used in structural design per ASCE standards. ASCE Amplify also supports advocacy, connecting civil engineers with elected officials to advocate for infrastructure investment and sustainable practices.
features:
- description: Query any US location by latitude and longitude or address to retrieve site-specific environmental hazard values for structural design, including ASCE 7 seismic, wind, snow, and ice parameters.
  name: Geographic Hazard Lookup
- description: Retrieve seismic design parameters including Ss, S1, SMS, SM1, SDS, SD1, and spectral acceleration values per ASCE 7 for any US location.
  name: ASCE 7 Seismic Parameters
- description: Access design wind speed values for various risk categories and exposure categories per ASCE 7 for structural wind load calculations.
  name: Wind Speed Data
- description: Retrieve ground snow load values and ice storm data for design of roof structures and overhead transmission lines per ASCE 7.
  name: Snow and Ice Load Data
- description: Tools for ASCE members to contact elected officials and advocate for infrastructure funding, engineering standards, and professional issues.
  name: Civil Engineer Advocacy
finops:
- name: Asce Amplify Finops
  service_category: API
  slug: asce-amplify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asce-amplify.png
integrations:
- description: API values directly correspond to ASCE 7 Minimum Design Loads for Buildings and Other Structures, the primary reference standard for US structural engineering.
  name: ASCE 7 Standards
- description: Hazard parameters from the API align with International Building Code requirements that reference ASCE 7 for environmental load design values.
  name: IBC Building Codes
layout: provider
modified: '2026-04-19'
name: ASCE Amplify
nav: Providers
network: true
overview: 'ASCE Amplify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Civil Engineering, Hazard Data, Engineering Standards, and Infrastructure.


  ASCE Amplify''s developer surface includes developer portal and 2 more developer resources.'
plans:
- name: Asce Amplify Plans Pricing
  plan_count: 3
  slug: asce-amplify-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Asce Amplify Rate Limits
  slug: asce-amplify-rate-limits
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asce-amplify/refs/heads/main/screenshots/asce-amplify-2026-06-20T172456.png
security:
- kind: domain-security
  name: Asce Amplify Domain Security
  slug: asce-amplify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asce-amplify
tags:
- Civil Engineering
- Hazard Data
- Engineering Standards
- Infrastructure
use_cases:
- description: Structural engineers use the ASCE Hazard Tool API to obtain site-specific hazard parameters for building and infrastructure design in compliance with ASCE 7 and building codes.
  name: Structural Design
- description: Civil engineers perform preliminary site assessments for new construction projects by querying multiple locations for hazard comparisons.
  name: Site Assessment
- description: Structural engineering software vendors integrate the ASCE Hazard Tool API to automatically populate design parameters based on project location.
  name: Software Integration
website: https://amplify.asce.org/
---
