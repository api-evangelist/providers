---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Provides access to the last 45 days of meteorological and oceanographic observations from NDBC moored buoys and C-MAN coastal stations. Data files are served via HTTPS at https://www.ndbc.noaa.gov/dat
  name: NDBC Real-Time Data Service
  slug: realtime-data-service
- description: Delivers a consolidated snapshot of the most recent observation from every active NDBC and partner station, refreshed every five minutes. The flat text file at https://www.ndbc.noaa.gov/data/latest_ob
  name: NDBC Latest Observations Service
  slug: latest-observations-service
- description: Provides quality-controlled historical observations from NDBC stations organized as annual files (prior years) and monthly files (current year) accessible at https://www.ndbc.noaa.gov/data/historical/
  name: NDBC Historical Archive Service
  slug: historical-archive-service
- description: Exposes NDBC station time-series data as NetCDF files through a THREDDS Data Server (TDS) at https://dods.ndbc.noaa.gov/ using the OPeNDAP protocol. Dataset categories include standard meteorology (st
  name: NDBC THREDDS/OPeNDAP NetCDF Service
  slug: thredds-netcdf-service
- description: Provides near-real-time ocean surface current speeds and directions derived from High-Frequency (HF) radar systems operated by NDBC and partner networks in various nearshore areas of the United States
  name: NDBC HF Radar Surface Currents Service
  slug: hf-radar-service
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ndbc-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.ndbc.noaa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ndbc.noaa.gov/docs/ndbc_web_data_guide.pdf
- group: docs
  title: ''
  type: Documentation
  url: https://www.ndbc.noaa.gov/faq/rt_data_access.shtml
- group: docs
  title: ''
  type: Documentation
  url: https://www.ndbc.noaa.gov/faq/measdes.shtml
- group: docs
  title: ''
  type: Documentation
  url: https://www.ndbc.noaa.gov/faq/stations.shtml
- group: operate
  title: ''
  type: Contact
  url: https://www.ndbc.noaa.gov/contacts.shtml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.noaa.gov/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.noaa.gov/disclaimer
- group: commercial
  title: ''
  type: Plans
  url: /plans/free.md
- group: operate
  title: ''
  type: RateLimits
  url: /rate-limits/rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: /finops/finops.md
created: '2026-06-13'
description: The NOAA National Data Buoy Center (NDBC) operates a global network of over 1,000 moored buoys, drifting buoys, Coastal-Marine Automated Network (C-MAN) stations, and partner stations that continuously measure and transmit meteorological and oceanographic conditions. Real-time and historical data — wind direction and speed, wave height and period, sea surface temperature, atmospheric pressure, air temperature, dew point, visibility, and salinity — are distributed freely via HTTP file URLs, a THREDDS/OPeNDAP server (NetCDF), an RSS observation feed, and a latest-observations snapshot updated every five minutes. No API key or authentication is required; data is in the public domain under U.S. government open-data policy.
image: https://www.ndbc.noaa.gov/images/nws/nws_logo.png
layout: provider
modified: '2026-06-13'
name: NDBC — National Data Buoy Center
nav: Providers
network: true
overview: 'NDBC — National Data Buoy Center publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include NOAA, Marine, Buoys, Ocean, and Weather.


  NDBC — National Data Buoy Center''s developer surface includes developer portal, documentation, and 10 more developer resources.'
random_paper: 79
score:
  band: emerging
  composite: 16.7
  delta: -2.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ndbc/refs/heads/main/screenshots/ndbc-2026-06-20T190220.png
security:
- kind: domain-security
  name: Ndbc Domain Security
  slug: ndbc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ndbc
tags:
- NOAA
- Marine
- Buoys
- Ocean
- Weather
- Waves
- Meteorological
- Oceanographic
- Real-Time
- Historical
- Government
- Open Data
website: https://www.ndbc.noaa.gov/
---
