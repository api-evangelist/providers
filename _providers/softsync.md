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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/softsync/hosts/softsync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/softsync-hosts.yml
- group: auth
  href: https://artifacts.apis.io/softsync/security/softsync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/softsync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://softsync.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://softsync.io/user-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://help.scopicsoftware.com/portal/en/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://softsync.io/index.php/privacy-terms-of-use/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://softsync.io/index.php/privacy-terms-of-use/
- group: commercial
  title: ''
  type: Pricing
  url: https://softsync.io/softsync-vs-unito
coverage:
  checked: '2026-10-21'
  detail: Provider's developer portal pages are rendered via JavaScript, preventing machine-readable spec extraction.
  evidence:
  - status: 200
    url: https://softsync.io/user-guide/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Scopic, operating under the SoftSync brand, provides a powerful integration platform that synchronizes project data between Jira Cloud and Teamwork. The solution enables bidirectional and unilateral sync of issues, tasks, comments, files, and custom fields, helping teams streamline workflows, reduce manual effort, and maintain data consistency across tools. SoftSync offers customizable synchronization settings, secure data handling, and support for global teams, positioning itself as a versatile automation tool for project management.
image: https://softsync.io/wp-content/uploads/2020/12/social_sharing_image-1.jpg
layout: provider
modified: '2026-10-21'
name: Scopic
nav: Providers
network: true
overview: 'Scopic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Project Management, Automation, Jira, and Teamwork.


  Scopic''s developer surface includes documentation, pricing, and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Softsync Domain Security
  slug: softsync-domain-security
  summary_line: TLSv1.3
slug: softsync
tags:
- Integration
- Project Management
- Automation
- Jira
- Teamwork
website: https://softsync.io/
---
