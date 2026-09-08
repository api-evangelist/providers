---
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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.actiumhealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.actiumhealth.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.actiumhealth.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actiumhealth.com/privacy-policy/
- group: start
  title: ''
  type: Demo
  url: https://www.actiumhealth.com/demo/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.actiumhealth.com/case-studies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/actiumhealth/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@actiumhealth
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actium-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/actium-health-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/actium-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/actium-health-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/actium-health-plans-pricing.yml
coverage:
  checked: '2026-09-06'
  detail: 'ActiumHealth is a division of Syllable Corporation - its own cookie policy says so verbatim - and it runs no developer program on actiumhealth.com: a crawl of all 58 sitemap URLs returned zero occurrences of FHIR, HL7, OpenAPI, Swagger, GraphQL, "API key" or "developer portal", no api./docs./developer./app. subdomain resolves, and all eighteen /.well-known/ probes across the apex and www hosts 404d, while the platform''s actual API, SDKs, CLI, MCP server and agent card are published by the parent at docs.syllable.ai and are already catalogued in this network as `syllable`.'
  evidence:
  - status: 200
    url: https://www.actiumhealth.com/sitemap.xml
  - status: 404
    url: https://www.actiumhealth.com/openapi.json
  - status: 404
    url: https://www.actiumhealth.com/.well-known/api-catalog
  - status: 200
    url: https://www.actiumhealth.com/cookie-policy/
  - status: 0
    url: https://api.actiumhealth.com/
  - status: 200
    url: https://docs.syllable.ai/
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: ActiumHealth is the conversational AI platform for healthcare patient communication, operated as a division of Syllable Corporation. Its voice, SMS, chat and email agents automate inbound and outbound patient calls across appointment scheduling, prescription refill, call routing, referral management, patient surveys, care coordination and revenue cycle workflows for health systems, patient access centers, healthcare contact centers and practice groups, with more than 70 million calls reported handled. The agents integrate with Epic, Cerner and Meditech EHRs through those vendors' APIs, and the platform is marketed as built to SOC 2, HITRUST and HIPAA standards. ActiumHealth consumes EHR APIs rather than publishing one and runs no developer program on actiumhealth.com; the underlying agentic platform API, SDKs, CLI, MCP server and documentation are published by its parent at syllable.ai and catalogued here as `syllable`.
image: https://www.actiumhealth.com/assets/images/social-share.png
layout: provider
modified: '2026-09-06'
name: Actium Health
nav: Providers
network: true
overview: 'Actium Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Engagement, Conversational AI, and Voice.


  Actium Health''s developer surface includes engineering blog, support, YouTube channel, and 10 more developer resources.'
plans:
- name: Actium Health Plans Pricing
  plan_count: 0
  slug: actium-health-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Actium Health Domain Security
  slug: actium-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: actium-health
tags:
- Company
- Healthcare
- Patient Engagement
- Conversational AI
- Voice
- Contact Center
- Artificial Intelligence
- Patient Access
- Health Systems
website: https://www.actiumhealth.com/
---
