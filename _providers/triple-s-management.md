---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Mi Triple-S is the online provider portal for Triple-S Salud, offering healthcare providers access to insured eligibility verification, claims and payments management, re-credentialing, and provider d
  name: Triple-S Salud Provider Portal
  slug: triple-s-salud-provider-portal
- description: Provider resources for Triple-S Advantage, the Medicare Advantage plan operated by Triple-S in Puerto Rico, including eligibility, prior authorizations, and claims management tools.
  name: Triple-S Advantage Provider Information
  slug: triple-s-advantage-provider-portal
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triple-s-management-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triple-s-management
- group: company
  title: ''
  type: Website
  url: https://www.triple-s-management.com
- group: company
  title: ''
  type: Website
  url: https://management.grupotriples.com/en/
- group: other
  title: ''
  type: Triple-S Salud
  url: https://salud.grupotriples.com/en/
- group: other
  title: ''
  type: Triple-S Advantage
  url: https://advantage.grupotriples.com/en/
- group: other
  title: ''
  type: Triple-S Vida
  url: https://vida.grupotriples.com/en/
- group: start
  title: ''
  type: Provider Portal
  url: https://service.ssspr.com/provider/login.aspx
- group: other
  title: ''
  type: Credentialing Platform
  url: https://www.ocshc.com/
- group: start
  title: ''
  type: Payment Portal
  url: https://ts.assertus.com/auth/login/index/
- group: start
  title: ''
  type: Member Portal
  url: https://salud.grupotriples.com/en/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/triple-s-management-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/triple-s-management-context.jsonld
- group: other
  title: ''
  type: x-profiled
  url: 2026-05
created: '2026-03-24'
description: Triple-S Management Corporation is the largest managed care company in Puerto Rico in terms of membership, providing health, life, and property and casualty insurance. A subsidiary of GuideWell (parent of Florida Blue), Triple-S operates as an independent licensee of the Blue Cross Blue Shield Association for Puerto Rico and the U.S. Virgin Islands. Its subsidiaries include Triple-S Salud (managed care), Triple-S Advantage (Medicare Advantage), Triple-S Vida (life insurance), Triple-S Propiedad (property and casualty), Salus (medical clinics), and CarePoint (IPA).
finops:
- name: Triple S Management Finops
  service_category: API
  slug: triple-s-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triple-s-management.png
json_schemas:
- name: Triple-S Management Health Plan Member
  property_count: 11
  slug: triple-s-management-member
json_structures:
- name: Triple S Management Member Structure
  property_count: 0
  slug: triple-s-management-member-structure
jsonld:
- class_count: 21
  name: Triple S Management Context
  property_count: 0
  slug: triple-s-management-context
layout: provider
modified: '2026-05-03'
name: Triple-S Management
nav: Providers
network: true
overview: 'Triple-S Management publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Health Insurance, Managed Care, Medicare Advantage, Puerto Rico, and Blue Cross Blue Shield.


  The Triple-S Management catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Triple S Management Plans Pricing
  plan_count: 3
  slug: triple-s-management-plans-pricing
press:
- date: '2026-05-25'
  title: Revenue for Triple-S Management (GTS)
  url: https://companiesmarketcap.com/triple-s-management/revenue/
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1171662/000095010321012760/dp156655_8k.htm
- date: '2026-05-25'
  title: GuideWell to Acquire Triple-S Management in ...
  url: https://www.prnewswire.com/news-releases/guidewell-to-acquire-triple-s-management-in-combination-designed-to-drive-health-care-affordability-and-improve-health-outcomes-in-florida-and-puerto-rico-301361460.html
- date: '2026-05-25'
  title: Triple-S, MCS, Liberty announce Puerto Rico hires
  url: https://newsismybusiness.com/triple-s-mcs-liberty-announce-puerto-rico-hires/
- date: '2026-05-25'
  title: Health Insurance Company Seeks Supreme Court Review ...
  url: https://www.taxnotes.com/research/federal/court-documents/court-petitions-and-briefs/health-insurance-company-seeks-supreme-court-review-of-decision-to/wkvm
random_paper: 106
rate_limits:
- limit_count: 5
  name: Triple S Management Rate Limits
  slug: triple-s-management-rate-limits
rules:
- name: Triple-S Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: triple-s-management-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 28.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triple-s-management/refs/heads/main/screenshots/triple-s-management-2026-06-20T195730.png
security:
- kind: domain-security
  name: Triple S Management Domain Security
  slug: triple-s-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: triple-s-management
tags:
- Health Insurance
- Managed Care
- Medicare Advantage
- Puerto Rico
- Blue Cross Blue Shield
- Healthcare
website: https://www.triple-s-management.com
---
