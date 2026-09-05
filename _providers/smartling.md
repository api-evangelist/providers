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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 59
  human_in_the_loop: 2
  name: Smartling Agentic Access
  operation_count: 109
  slug: smartling-agentic-access
  summary_line: 109 operations · 59 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Smartling's REST API for the translation management platform. Resource groups include Authentication, Accounts, Projects, Source Files, Strings, Translations, Jobs, Glossary, Issues, Quality Checks, M
  name: Smartling REST API
  slug: api-v2
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: Each client within Smartling is given their own account with a designated `accountUid`. Within each account is any number of projects. All files, content, and jobs are tied to a particular project. Th
  name: Smartling Account & Projects API
  slug: smartling-account-projects-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: 'The Attachments API allows for file attachment upload, download and checking linked attachments for an entity. Attachment entities can be from three domains: strings, jobs or issues. Each entity is re'
  name: Smartling Attachments API
  slug: smartling-attachments-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: Smartling uses OAuth2 for [authentication](https://help.smartling.com/hc/en-us/articles/1260805176849). To access the Smartling APIs, you'll first need to authenticate with your user identifier and us
  name: Smartling Authentication API
  slug: smartling-authentication-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The Content Search API allows you to search for strings within a Smartling project. You can filter by string text, hashcode, namespace, or any combination of available filters.
  name: Smartling Content Search API
  slug: smartling-content-search-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: '[Visual context](https://help.smartling.com/hc/en-us/articles/360057484273) helps Translators make linguistic, layout, and spacing decisions based on where strings appear in your mobile or desktop app'
  name: Smartling Context API
  slug: smartling-context-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The Estimates API from Smartling — 6 operation(s) for estimates.
  name: Smartling Estimates API
  slug: smartling-estimates-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: 'Files are typically how you can exchange your content with Smartling to get translations. Smartling supports a wide variety of [file types](https://help.smartling.com/hc/en-us/articles/360007998893). '
  name: Smartling Files API
  slug: smartling-files-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The GDN url management API from Smartling — 4 operation(s) for gdn url management.
  name: Smartling GDN url management API
  slug: smartling-gdn-url-management-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: A Smartling project (such as a mobile, web, files, or connector project) may contain one or more [jobs](https://help.smartling.com/hc/en-us/articles/1260805481390). You may have multiple projects, eac
  name: Smartling Jobs API
  slug: smartling-jobs-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The Language Detection API from Smartling — 1 operation(s) for language detection.
  name: Smartling Language Detection API
  slug: smartling-language-detection-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: Locales are the language and country pairs that are used to identify the source content and the desired target locale for your translated content.
  name: Smartling Locales API
  slug: smartling-locales-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The Smartling platform offers state-of-the-art [Machine Translation capabilities](https://www.smartling.com/software/neural-machine-translation-hub/) through its synchronous account-level Machine Tran
  name: Smartling Machine Translation (MT) API
  slug: smartling-machine-translation-mt-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: Smartling users, who process and translate content with the Smartling platform.
  name: Smartling People API
  slug: smartling-people-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The Reports API allows to request various reports available on Smartling platform and specify additional filtering criteria to narrow down data returned by the reports.
  name: Smartling Reports API
  slug: smartling-reports-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: A string is a piece of translation. Based on the source content, strings can be parsed differently. A string is then broken down further, into one or more segments. The Strings API allows you to direc
  name: Smartling Strings API
  slug: smartling-strings-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: Tags can help you manage your strings. The Tags API allows you to add/remove string tags, and search for tags in a project.
  name: Smartling Tags API
  slug: smartling-tags-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The Vendors API is for Language Service Providers to view work that's available in Smartling.
  name: Smartling Vendors API
  slug: smartling-vendors-api
- baseURL: https://api.smartling.com
  baseurl_source: declared
  description: The Workflow Assignment API handles workflow step assignments for non agency users.
  name: Smartling Workflow Assignment API
  slug: smartling-workflow-assignment-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smartling REST API Reference Account & Projects API
  slug: open-smartling-account-projects-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Attachments API
  slug: open-smartling-attachments-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Authentication API
  slug: open-smartling-authentication-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Content Search API
  slug: open-smartling-content-search-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Context API
  slug: open-smartling-context-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Estimates API
  slug: open-smartling-estimates-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Files API
  slug: open-smartling-files-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects GDN url management API
  slug: open-smartling-gdn-url-management-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Jobs API
  slug: open-smartling-jobs-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Language Detection API
  slug: open-smartling-language-detection-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Locales API
  slug: open-smartling-locales-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Machine Translation (MT) API
  slug: open-smartling-machine-translation-mt-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects People API
  slug: open-smartling-people-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Reports API
  slug: open-smartling-reports-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Strings API
  slug: open-smartling-strings-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Tags API
  slug: open-smartling-tags-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Vendors API
  slug: open-smartling-vendors-api
- collection_type: open
  name: Smartling REST API Reference Account & Projects Workflow Assignment API
  slug: open-smartling-workflow-assignment-api
- collection_type: open
  name: Smartling REST API Reference
  slug: open-smartling
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartling-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smartling-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartling-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartling.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-reference.smartling.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.smartling.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Smartling
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartling
- group: commercial
  title: ''
  type: Plans
  url: plans/smartling-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smartling-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smartling-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.smartling.com/blog/rss.xml
created: '2026-05-23'
description: Smartling is an enterprise translation management platform combining a cloud-based TMS, LinguisticAI, and neural machine translation. The Smartling REST API at api.smartling.com exposes authentication, accounts, projects, source files, strings, translations, jobs, glossary, issues, quality checks, MT, and reports. Authentication uses an OAuth-style userIdentifier + secret pair that returns a short-lived bearer access token (~5-10 minute TTL) with a refresh token.
finops:
- name: Smartling Finops
  service_category: API
  slug: smartling-finops
graphqls:
- description: Smartling is a translation management system for global content. The API covers project management, file upload and download, translation jobs, glossary management, visual context, translation memory,
  name: Smartling GraphQL API
  slug: smartling-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartling.png
layout: provider
modified: '2026-05-23'
name: Smartling
nav: Providers
network: true
overview: 'Smartling publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Account & Projects API, Attachments API, Authentication API, and 15 more. Tagged areas include Localization, Translation, TMS, LinguisticAI, and Neural MT.


  Smartling''s developer surface includes documentation, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Smartling Plans Pricing
  plan_count: 1
  slug: smartling-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Smartling Rate Limits
  slug: smartling-rate-limits
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 57.2
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartling/refs/heads/main/screenshots/smartling-2026-06-20T194043.png
security:
- kind: domain-security
  name: Smartling Domain Security
  slug: smartling-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Smartling Trust Center
  slug: smartling-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: smartling
tags:
- Localization
- Translation
- TMS
- LinguisticAI
- Neural MT
- Enterprise
- REST
website: https://www.smartling.com/
---
