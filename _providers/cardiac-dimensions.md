---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardiac-dimensions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardiacdimensions.com/
coverage:
  checked: '2026-08-09'
  detail: Cardiac Dimensions manufactures the CARILLON Mitral Contour System, an implantable Class III cardiac device, and certificate-transparency enumeration of every certificate ever issued for cardiacdimensions.com returns only mail, autodiscover, sslvpn, staging1/2 and www hosts — no api, developer, docs or portal hostname has ever existed — while the WordPress marketing site itself answers every path, including the homepage, with a SiteGround sgcaptcha interstitial.
  evidence:
  - status: 200
    url: https://crt.sh/json?q=cardiacdimensions.com
  - status: 202
    url: https://cardiacdimensions.com/developers
  - status: 202
    url: https://cardiacdimensions.com/openapi.json
  - status: 202
    url: https://cardiacdimensions.com/.well-known/agent-card.json
  - status: 404
    url: https://github.com/cardiacdimensions
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: Cardiac Dimensions is a privately held structural-heart medical device company headquartered in Kirkland, Washington, developing transcatheter therapies for patients with heart failure and functional mitral regurgitation. Its lead product is the CARILLON Mitral Contour System, a minimally invasive, catheter-delivered implant placed in the coronary sinus to reshape the mitral valve annulus and reduce functional mitral regurgitation without open-heart surgery. CARILLON carries a CE Mark in Europe and remains an investigational device in the United States, where the company is completing the EMPOWER pivotal trial. Cardiac Dimensions closed an oversubscribed $53M Series E in March 2025 led by Ally Bridge Group. The company manufactures an implantable Class III medical device and operates no public developer program, API, or software platform.
layout: provider
modified: '2026-08-09'
name: Cardiac Dimensions
nav: Providers
network: true
overview: Cardiac Dimensions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Cardiology, Heart Failure, and Structural Heart.
random_paper: 97
score:
  band: minimal
  composite: 5.1
  delta: 0.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Cardiac Dimensions Domain Security
  slug: cardiac-dimensions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardiac-dimensions
tags:
- Company
- Medical Devices
- Cardiology
- Heart Failure
- Structural Heart
- Transcatheter
- Health Care
- Medical Technology
website: https://cardiacdimensions.com/
---
