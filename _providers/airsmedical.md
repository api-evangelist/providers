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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://airsmed.com
- group: company
  title: ''
  type: About
  url: https://airsmed.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://airsmed.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://airsmed.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://airsmed.com/leadership/
- group: operate
  title: ''
  type: Support
  url: https://airsmed.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://airsmed.com/faq/
- group: company
  title: ''
  type: Careers
  url: https://airsmed.com/careers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://airsmed.com/releasenote/swiftmr/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/changelog/airsmedical-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/airsmedical-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://airsmed.com/compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/security/airsmedical-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/airsmedical-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/conformance/airsmedical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airsmedical-conformance.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airsmed.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airsmed.com/terms-and-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airsmedical
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airsmed/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@airsmedical
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/llms/airsmedical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airsmedical-llms.txt
- group: design
  title: ''
  type: AccessibilityConformance
  url: https://airsmed.com/accessibility-statement/
- group: other
  title: ''
  type: AITransparency
  url: https://airsmed.com/ai-transparency-statement/
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://airsmed.com/privacy-policy/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://airsmed.com/privacy-rights-inquiries/
- group: operate
  title: ''
  type: IncidentNotification
  url: https://airsmed.com/privacy-policy/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/regulatory/airsmedical-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airsmedical-regulatory-posture.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/plans/airsmedical-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airsmedical-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/rate-limits/airsmedical-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airsmedical-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airsmedical/refs/heads/main/security/airsmedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airsmedical-domain-security.yml
coverage:
  checked: '2026-09-19'
  detail: AIRS Medical ships regulated medical-device software (SwiftMR, SwiftSight) that talks DICOM to the scanner and PACS on the hospital network; airsmed.com has no developer, API or docs path (all 404), no OpenAPI/GraphQL/MCP/agent-card at any discovery location, and its GitHub org holds an ITK-SNAP fork and a DLP plugin rather than an SDK.
  evidence:
  - status: 404
    url: https://airsmed.com/developers
  - status: 404
    url: https://airsmed.com/openapi.json
  - status: 404
    url: https://airsmed.com/.well-known/agent-card.json
  - status: 200
    url: https://airsmed.com/faq/
  - status: 200
    url: https://api.github.com/orgs/airsmedical
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: AIRS Medical (AI Radiology Solutions) is a Seoul-founded medical-AI company whose SwiftMR deep-learning MRI reconstruction software cuts scan times by up to 50% on existing scanners, and whose SwiftSight products deliver quantitative brain, DTI and body-composition reporting. SwiftMR is FDA 510(k)-cleared, CE-marked under EU MDR, PMDA-approved and MDSAP-certified, and is deployed at 1,700+ institutions in 40+ countries. The products integrate with hospital MRI scanners and PACS over the DICOM protocol (SwiftMR presents itself to the scanner as a PACS node); the company publishes no public developer program, API, SDK or webhooks.
image: https://airsmed.com/wp-content/uploads/2023/05/AIRS-Medical_Logo_RGB_Symbol.png
layout: provider
modified: '2026-09-19'
name: AIRS Medical
nav: Providers
network: true
overview: 'AIRS Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Imaging, MRI, and Radiology.


  AIRS Medical''s developer surface includes engineering blog, support, changelog, YouTube channel, and 24 more developer resources.'
plans:
- name: Airsmedical Plans Pricing
  plan_count: 0
  slug: airsmedical-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Airsmedical Rate Limits
  slug: airsmedical-rate-limits
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 18.4
  previous_composite: 22.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 40.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airsmedical Domain Security
  slug: airsmedical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Airsmedical Trust Center
  slug: airsmedical-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type II, HIPAA, GDPR, ISO/IEC 42001, FDA 510(k), CE Marking (EU MDR), PMDA approval (Japan), MDSAP
slug: airsmedical
tags:
- Company
- Healthcare
- Medical Imaging
- MRI
- Radiology
- Artificial Intelligence
- Medical Devices
- DICOM
website: https://airsmed.com
---
