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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Brightchamps offers an education platform; API details are not publicly documented.
  name: Brightchamps API
  slug: brightchamps-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brightchamps/refs/heads/main/llms/brightchamps-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brightchamps-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightchamps/refs/heads/main/hosts/brightchamps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brightchamps-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightchamps/refs/heads/main/vendors/brightchamps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brightchamps-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brightchamps.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://champ.brightchamps.com/login/?redirectUrl=https%3A%2F%2Fbrightchamps.com
- group: other
  title: ''
  type: Leadership
  url: https://brightchamps.com/en-us/team
- group: company
  title: ''
  type: Blog
  url: https://brightchamps.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BrightChamps
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brightchamps/refs/heads/main/security/brightchamps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightchamps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brightchamps.com
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at any discovered host.
  evidence:
  - status: 0
    url: https://api.brightchamps.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Brightchamps is an education technology company focused on teaching coding, robotics, financial literacy, and other future‑ready skills to children through online and in‑person programs. Their platform offers a variety of courses, including coding classes, robotics, math, generative AI, and soft‑skill development, aiming to empower the next generation with practical tech knowledge. Brightchamps serves families worldwide, providing flexible learning paths and resources for both kids and educators.
image: https://d26kej74xcgneg.cloudfront.net/brightchamps-new-website/brightchamps_logo_without_tagline.png
layout: provider
modified: '2026-10-06'
name: Brightchamps
nav: Providers
network: true
overview: 'Brightchamps is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Kids, and Coding.


  Brightchamps'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brightchamps Domain Security
  slug: brightchamps-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: brightchamps
tags:
- Company
- Education
- EdTech
- Kids
- Coding
- Robotics
website: https://brightchamps.com
---
