---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: OAI-PMH metadata harvesting endpoint documented for UT Research Information, the University of Twente's Pure-based research information system at research.utwente.nl. It is intended to expose research
  name: UT Research Information (Pure) OAI-PMH
  slug: pure-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-twente-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-twente-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.utwente.nl/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/utwente
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-twente/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/utwente-fmt
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-twente-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-twente-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-twente-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Twente (Universiteit Twente, UT), founded in 1961 in Enschede, Netherlands, is a public technical research university and ranks #233 in the QS World University Rankings 2025. Its publicly confirmable developer/API footprint is modest. The university runs a Pure-based research information system, UT Research Information (research.utwente.nl), which is documented as exposing an OAI-PMH metadata harvesting endpoint, though that endpoint is not openly reachable from the public web front-end at time of review. Source code from the university and its research groups is published across several GitHub organizations. The University of Twente is also a co-founding member of the 4TU.ResearchData repository (data.4tu.nl), which is hosted and governed by TU Delft rather than operated by UT itself.'
finops:
- name: University Of Twente Finops
  service_category: Education
  slug: university-of-twente-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-twente.png
jsonld:
- class_count: 7
  name: University Of Twente Context
  property_count: 3
  slug: university-of-twente-context
layout: provider
modified: '2026-06-03'
name: University of Twente
nav: Providers
network: true
overview: 'University of Twente publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Netherlands.


  The University of Twente catalog on APIs.io includes 1 JSON-LD context.


  University of Twente''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: University Of Twente Plans Pricing
  plan_count: 2
  slug: university-of-twente-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of Twente Rate Limits
  slug: university-of-twente-rate-limits
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-twente/refs/heads/main/screenshots/university-of-twente-2026-06-20T200328.png
security:
- kind: domain-security
  name: University Of Twente Domain Security
  slug: university-of-twente-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Twente Vulnerability Disclosure
  slug: university-of-twente-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-twente
tags:
- Education
- Higher Education
- University
- Research Data
- Netherlands
- Open Science
website: https://www.utwente.nl/en/
---
