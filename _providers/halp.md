---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://halp.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.atlassian.com/software/jira/service-management/help-desk-software-small-business-software — a different registrable domain (halp.com -> atlassian.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halp-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/halp-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/halp-security.txt
- group: company
  title: ''
  type: Website
  url: https://halp.com/
created: '2026-07-17'
description: Halp was a conversational ticketing and help-desk tool that let teams turn Slack and Microsoft Teams messages into trackable tickets, founded in Boulder, Colorado and backed by Techstars. Atlassian acquired Halp in February 2020 and folded its capabilities into Jira Service Management; the standalone Halp product and its API were subsequently discontinued. The halp.com domain now resolves to Atlassian and is served from Atlassian's edge, so no independent Halp developer portal, API reference, SDKs, or MCP surface remains to enrich. This profile records the company's history and the (Atlassian-operated) security posture still observable on the halp.com domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/halp.png
layout: provider
modified: '2026-07-19'
name: Halp
nav: Providers
network: true
overview: Halp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Help Desk, Ticketing, Customer-Support, and Slack.
random_paper: 1
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/halp/refs/heads/main/screenshots/halp-2026-07-25T220553.png
security:
- kind: domain-security
  name: Halp Domain Security
  slug: halp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: halp
tags:
- Company
- Help Desk
- Ticketing
- Customer-Support
- Slack
- Microsoft Teams
- Conversational
- Acquired
website: https://halp.com/
---
