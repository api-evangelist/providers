---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bored Agentic Access
  operation_count: 14
  slug: bored-agentic-access
  summary_line: 14 operations · 1 acting
api_count: 5
apis:
- description: Random and filtered activity suggestions.
  name: Bored API Activities API
  slug: bored-activities-api
- description: Random or keyed factual snippets (v2 only).
  name: Bored API Facts API
  slug: bored-facts-api
- description: Random or keyed riddles with difficulty filter (v2 only).
  name: Bored API Riddles API
  slug: bored-riddles-api
- description: Community-submitted content suggestions for review (v2 only).
  name: Bored API Suggestions API
  slug: bored-suggestions-api
- description: Random or keyed website recommendations (v2 only).
  name: Bored API Websites API
  slug: bored-websites-api
artifact_total: 47
collections:
- collection_type: open
  name: Bored API
  slug: open-bored-api
- collection_type: open
  name: Bored API (App Brewery Fork)
  slug: open-bored-appbrewery
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bored-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bored-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boredapi.com/
- group: start
  title: ''
  type: Portal
  url: https://bored-api.appbrewery.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/drewthoennes/Bored-API
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/drewthoennes/Bored-API
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/drewthoennes/Bored-API#readme
- group: commercial
  title: ''
  type: License
  url: https://github.com/drewthoennes/Bored-API/blob/master/license
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/bored/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/bored-api/
- group: build
  title: ''
  type: SDKs
  url: https://gitlab.com/CMDR_Tvis/bored-api
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bored-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/bored-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bored-vocabulary.yml
created: '2026-05-28'
description: The Bored API is a free, open-source, no-authentication public API that serves suggestions for things to do when you are bored. The canonical reference implementation is an MEVN (MongoDB / Express / Vue / Node) project maintained by Drew Thoennes at github.com/drewthoennes/Bored-API (MIT licensed). The historically hosted instance at https://www.boredapi.com/ has been intermittently or fully unreachable since June 2024 (originally hosted on Heroku); a community fork maintained by The App Brewery at https://bored-api.appbrewery.com remains actively available for students and consumers. This profile documents the v1 surface (legacy activities-only), the v2 surface (activities + facts + riddles + websites + suggestions), and the App Brewery community mirror, so the API contract is preserved as a historical, self-hostable artifact.
examples:
- key_count: 2
  name: Bored Api Get Activity By Key V2 Example
  slug: bored-api-get-activity-by-key-v2-example
- key_count: 2
  name: Bored Api Get Random Activity V1 Example
  slug: bored-api-get-random-activity-v1-example
- key_count: 2
  name: Bored Api Get Random Activity V1 Filtered Example
  slug: bored-api-get-random-activity-v1-filtered-example
- key_count: 2
  name: Bored Api Get Random Activity V2 Example
  slug: bored-api-get-random-activity-v2-example
- key_count: 2
  name: Bored Api Get Random Fact Example
  slug: bored-api-get-random-fact-example
- key_count: 2
  name: Bored Api Get Random Riddle Example
  slug: bored-api-get-random-riddle-example
- key_count: 2
  name: Bored Api Get Random Website Example
  slug: bored-api-get-random-website-example
- key_count: 2
  name: Bored Api Submit Suggestion Example
  slug: bored-api-submit-suggestion-example
- key_count: 2
  name: Bored Appbrewery Filter Example
  slug: bored-appbrewery-filter-example
- key_count: 2
  name: Bored Appbrewery Get Random Example
  slug: bored-appbrewery-get-random-example
features:
- description: No API key, no auth, no signup required.
  name: Free and open
- description: Activities can be filtered by type, participants, price, and accessibility — including min/max ranges.
  name: Multi-dimensional filtering
- description: V1 (legacy) and v2 (extended with facts, riddles, websites, suggestions) coexist.
  name: Versioned surface
- description: MIT-licensed MEVN stack — clone, npm install, run against a local MongoDB.
  name: Self-hostable
- description: V2 suggestions endpoint accepts new activity, fact, riddle, and website submissions for moderator review.
  name: Community-extensible
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bored.png
integrations:
- description: I'm Bored Alexa skill consuming the Bored API for spoken suggestions.
  name: Amazon Alexa
- description: bored and bored-api Python wrappers on PyPI.
  name: Python (PyPI)
- description: CMDR_Tvis Kotlin wrapper on GitLab.
  name: Kotlin
- description: Bored — Find What to Do iOS app.
  name: iOS App Store
- description: Used as the canonical fetch/axios teaching API in The App Brewery's web-development course.
  name: The App Brewery
json_schemas:
- name: BoredActivityV1
  property_count: 7
  slug: bored-activity-v1
- name: BoredActivityV2
  property_count: 9
  slug: bored-activity-v2
- name: BoredFact
  property_count: 3
  slug: bored-fact
- name: BoredRiddle
  property_count: 5
  slug: bored-riddle
- name: BoredSuggestion
  property_count: 4
  slug: bored-suggestion
- name: BoredWebsite
  property_count: 3
  slug: bored-website
json_structures:
- name: Bored Activity V1 Structure
  property_count: 7
  slug: bored-activity-v1-structure
- name: Bored Activity V2 Structure
  property_count: 9
  slug: bored-activity-v2-structure
- name: Bored Fact Structure
  property_count: 3
  slug: bored-fact-structure
- name: Bored Riddle Structure
  property_count: 5
  slug: bored-riddle-structure
- name: Bored Website Structure
  property_count: 3
  slug: bored-website-structure
jsonld:
- class_count: 0
  name: Bored Context
  property_count: 5
  slug: bored-context
layout: provider
modified: '2026-05-30'
name: Bored API
nav: Providers
network: true
overview: 'Bored API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Facts API, Riddles API, and 2 more. Tagged areas include Activities, Boredom, Community, Development, and Discovery.


  The Bored API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bored API''s developer surface includes developer portal, GitHub presence, documentation, and 12 more developer resources.'
random_paper: 50
rules:
- name: Bored API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bored-jsonschema-spectral-rules
- name: Bored API API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 4
  slug: bored-rules
score:
  band: thin
  composite: 39.0
  delta: -5.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 64.4
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bored/refs/heads/main/screenshots/bored-2026-06-20T173607.png
security:
- kind: domain-security
  name: Bored Domain Security
  slug: bored-domain-security
  summary_line: TLSv1.3
slug: bored
tags:
- Activities
- Boredom
- Community
- Development
- Discovery
- Education
- Facts
- Free
- MEVN
- No Auth
- Open Source
- Public APIs
- Recreation
- Riddles
- Suggestions
- Websites
use_cases:
- description: I'm Bored Alexa skill, Discord bots, browser extensions for spontaneous activity ideas.
  name: Boredom busters
- description: Sample API used in many web-development bootcamps (notably The App Brewery course) for fetch/axios/HTTP exercises.
  name: Teaching API
- description: iOS and Android apps that surface random activities to users.
  name: Mobile apps
- description: Helper tools that recommend low-cost, low-participant activities when users can't decide what to do.
  name: Decision support
website: https://www.boredapi.com/
---
