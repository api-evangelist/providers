---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-17'
api_count: 16
apis:
- description: Cloudshare provides a developer API documented at https://docs.cloudshare.com/.
  name: Cloudshare API
  slug: cloudshare-api-2
- description: The Class API from Cloudshare — 10 operation(s) for class.
  name: Cloudshare Class API
  slug: cloudshare-class-api
- description: The ClassAnalytics API from Cloudshare — 2 operation(s) for classanalytics.
  name: Cloudshare Class Analytics API
  slug: cloudshare-classanalytics-api
- description: The Cloudfolders API from Cloudshare — 2 operation(s) for cloudfolders.
  name: Cloudshare Cloudfolders API
  slug: cloudshare-cloudfolders-api
- description: The Cloudshare API API from Cloudshare — 1 operation(s) for cloudshare api.
  name: Cloudshare Cloudshare API
  slug: cloudshare-cloudshare-api-api
- description: The .. API from Cloudshare — 1 operation(s) for ...
  name: Cloudshare .. API
  slug: cloudshare-default-api
- description: The Envs API from Cloudshare — 2 operation(s) for envs.
  name: Cloudshare Envs API
  slug: cloudshare-envs-api
- description: The Externalclouds API from Cloudshare — 1 operation(s) for externalclouds.
  name: Cloudshare Externalclouds API
  slug: cloudshare-externalclouds-api
- description: The ID API from Cloudshare — 1 operation(s) for id.
  name: Cloudshare ID API
  slug: cloudshare-id-api
- description: The Instructors API from Cloudshare — 1 operation(s) for instructors.
  name: Cloudshare Instructors API
  slug: cloudshare-instructors-api
- description: The Invitations API from Cloudshare — 1 operation(s) for invitations.
  name: Cloudshare Invitations API
  slug: cloudshare-invitations-api
- description: The Projects API from Cloudshare — 3 operation(s) for projects.
  name: Cloudshare Projects API
  slug: cloudshare-projects-api
- description: The Snapshots API from Cloudshare — 3 operation(s) for snapshots.
  name: Cloudshare Snapshots API
  slug: cloudshare-snapshots-api
- description: The Users API from Cloudshare — 2 operation(s) for users.
  name: Cloudshare Users API
  slug: cloudshare-users-api
- description: The Vms API from Cloudshare — 2 operation(s) for vms.
  name: Cloudshare Vms API
  slug: cloudshare-vms-api
- description: The Webhooks API from Cloudshare — 1 operation(s) for webhooks.
  name: Cloudshare Webhooks API
  slug: cloudshare-webhooks-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/rules/cloudshare-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudshare-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/conformance/cloudshare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudshare-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/llms/cloudshare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudshare-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/well-known/cloudshare-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloudshare-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/well-known/cloudshare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudshare-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/hosts/cloudshare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudshare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/vendors/cloudshare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudshare-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/packages/cloudshare-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudshare-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/packages/cloudshare-packages.yml
  title: ''
  type: Packages
  url: packages/cloudshare-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.cloudshare.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudshare.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudshare.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudshare.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudshare.com/resources/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudshare.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudshare
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudshare/refs/heads/main/security/cloudshare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudshare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudshare.com
coverage:
  checked: '2026-10-09'
  detail: Documentation at https://docs.cloudshare.com/ is a JavaScript‑rendered page with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://docs.cloudshare.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: CloudShare provides virtual IT labs and hands‑on practice environments that enable software vendors, training providers, and enterprises to create realistic, on‑demand sandbox environments for demos, proofs‑of‑concept, onboarding, and cybersecurity training. Their AI‑first platform automates provisioning of complex multi‑application setups, allowing users to test, train, and showcase software without needing physical hardware.
image: https://www.cloudshare.com/wp-content/uploads/2023/01/post-logo-cloudshare.jpg
layout: provider
modified: '2026-10-09'
name: Cloudshare
nav: Providers
network: true
overview: 'Cloudshare is listed with 16 APIs on the [APIs.io](https://apis.io/) network, including Class API, Class Analytics API, Cloudfolders API, and 13 more. Tagged areas include Cloud, VirtualLabs, Training, Sandbox, and Enterprise.


  The Cloudshare catalog on APIs.io includes 1 Spectral governance ruleset.


  Cloudshare''s developer surface includes support, pricing, engineering blog, documentation, and 14 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Cloudshare API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: cloudshare-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 9.6
    developer_ergonomics: 23.8
    discoverability: 69.6
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Cloudshare Domain Security
  slug: cloudshare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudshare
tags:
- Cloud
- VirtualLabs
- Training
- Sandbox
- Enterprise
website: https://www.cloudshare.com
---
