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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octave-bioscience-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/octave-bioscience-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/octave-bioscience-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.octavebio.com/
- group: company
  title: ''
  type: About
  url: https://www.octavebio.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.octavebio.com/contact
- group: company
  title: ''
  type: News
  url: https://www.octavebio.com/news
- group: other
  title: ''
  type: Resources
  url: https://www.octavebio.com/resources
- group: company
  title: ''
  type: Careers
  url: https://www.octavebio.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.octavebio.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.octavebio.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.octavebio.com/trust-center
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/octave-bioscience_stock/
coverage:
  checked: '2026-08-04'
  detail: Octave Bioscience runs a Webflow marketing site for a lab-developed blood test; test ordering is a paper form or a provider contact form routed to Quest Diagnostics, and api./developer./docs./ portal./app.octavebio.com do not resolve in DNS, so there is no developer surface to read.
  evidence:
  - status: 404
    url: https://www.octavebio.com/openapi.json
  - status: 404
    url: https://www.octavebio.com/.well-known/api-catalog
  - status: 404
    url: https://www.octavebio.com/llms.txt
  - status: 200
    url: https://www.octavebio.com/providers
  - status: 200
    url: https://www.octavebio.com/trust-center
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: Octave Bioscience is a precision neurology company founded in 2014 and headquartered in Menlo Park, California, that develops blood-based multi-protein biomarker tests for chronic neurological disease. Its commercially available Octave Multiple Sclerosis Disease Activity (MSDA) Test measures a panel of serum proteins to produce a quantitative disease activity score used alongside clinical and imaging assessment, and is available across the United States through a strategic collaboration with Quest Diagnostics. The company is also developing a Multiple Sclerosis Disease Progression (MSDP) test and a Parkinson's disease biomarker assay supported by a Michael J. Fox Foundation grant. Octave publishes a public trust center documenting HITRUST, ISO/IEC 27001:2022, ISO/IEC 42001:2023, HIPAA and GDPR posture, but operates no public developer program, API reference, SDK or machine-readable specification.
image: https://cdn.prod.website-files.com/69ea29820ae8c216aa6d3eb3/69ee5d8d78bf430b8d8cc256_octave_logo.svg
layout: provider
modified: '2026-08-04'
name: Octave Bioscience
nav: Providers
network: true
overview: 'Octave Bioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Life Sciences, Diagnostics, and Neurology.


  Octave Bioscience''s developer surface includes support, product news, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.8
  delta: -0.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octave-bioscience/refs/heads/main/screenshots/octave-bioscience-2026-08-07T185938.png
security:
- kind: domain-security
  name: Octave Bioscience Domain Security
  slug: octave-bioscience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Octave Bioscience Trust Center
  slug: octave-bioscience-trust-center
  summary_line: HITRUST, ISO/IEC 27001:2022, ISO/IEC 42001:2023, HIPAA, GDPR
slug: octave-bioscience
tags:
- Company
- Health Care
- Life Sciences
- Diagnostics
- Neurology
- Precision Medicine
- Biotechnology
- Laboratory Testing
- Multiple Sclerosis
website: https://www.octavebio.com/
---
