---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Wordnik Agentic Access
  operation_count: 28
  slug: wordnik-agentic-access
  summary_line: 28 operations · 6 acting
api_count: 5
apis:
- description: API-key status and user authentication operations.
  name: Wordnik Account API
  slug: wordnik-account-api
- description: Operations on a single English word (definitions, etymologies, examples, pronunciations, related words, frequency, hyphenation, phrases, scrabble score, audio).
  name: Wordnik Word API
  slug: wordnik-word-api
- description: Read and write operations on an individual user word list.
  name: Wordnik Word List API
  slug: wordnik-word-list-api
- description: Create new user word lists.
  name: Wordnik Word Lists API
  slug: wordnik-word-lists-api
- description: Cross-word operations (random words, reverse-dictionary search, full-text search, word-of-the-day).
  name: Wordnik Words API
  slug: wordnik-words-api
artifact_total: 137
collections:
- collection_type: postman
  name: Wordnik Account API
  slug: postman-wordnik-account-api
- collection_type: postman
  name: Wordnik Account Word API
  slug: postman-wordnik-word-api
- collection_type: postman
  name: Wordnik Account Word List API
  slug: postman-wordnik-word-list-api
- collection_type: postman
  name: Wordnik Account Word Lists API
  slug: postman-wordnik-word-lists-api
- collection_type: postman
  name: Wordnik Account Words API
  slug: postman-wordnik-words-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wordnik Account API
  slug: open-wordnik-account-api
- collection_type: open
  name: Wordnik Account Word API
  slug: open-wordnik-word-api
- collection_type: open
  name: Wordnik Account Word List API
  slug: open-wordnik-word-list-api
- collection_type: open
  name: Wordnik Account Word Lists API
  slug: open-wordnik-word-lists-api
- collection_type: open
  name: Wordnik Account Words API
  slug: open-wordnik-words-api
- collection_type: open
  name: Wordnik
  slug: open-wordnik
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wordnik/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wordnik-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wordnik-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wordnik-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wordnik.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordnik.com
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.wordnik.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wordnik.com/gettingstarted
- group: start
  title: ''
  type: Signup
  url: https://www.wordnik.com/signup
- group: company
  title: ''
  type: Blog
  url: https://blog.wordnik.com
- group: operate
  title: ''
  type: StatusPage
  url: https://github.com/wordnik/wordnik-status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wordnik
- group: operate
  title: ''
  type: Support
  url: mailto:apiteam@wordnik.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wordnik.com/about
- group: commercial
  title: ''
  type: Plans
  url: plans/wordnik-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wordnik-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wordnik-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wordnik-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/wordnik-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/wordnik-context.jsonld
- group: other
  title: Wordnik Public Word List
  type: OpenSource
  url: https://github.com/wordnik/wordlist
- group: other
  title: NYT First Said
  type: OpenSource
  url: https://github.com/wordnik/nyt-first-said
- group: other
  title: Language Museums Dataset
  type: OpenSource
  url: https://github.com/wordnik/language-museums
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Wordnik is the largest online English dictionary by number of words. Its v4 REST API exposes definitions from five dictionaries, etymologies, real example sentences from millions of sources, audio pronunciations, related-word relationships, frequency over time, hyphenation, bi-gram phrases, scrabble scores, random words, reverse-dictionary lookup, word-of-the-day, and authenticated user word lists.
examples:
- key_count: 6
  name: Wordnik Api Token Status Example
  slug: wordnik-api-token-status-example
- key_count: 14
  name: Wordnik Audio File Example
  slug: wordnik-audio-file-example
- key_count: 2
  name: Wordnik Audio Type Example
  slug: wordnik-audio-type-example
- key_count: 3
  name: Wordnik Authentication Token Example
  slug: wordnik-authentication-token-example
- key_count: 5
  name: Wordnik Bigram Example
  slug: wordnik-bigram-example
- key_count: 2
  name: Wordnik Category Example
  slug: wordnik-category-example
- key_count: 2
  name: Wordnik Citation Example
  slug: wordnik-citation-example
- key_count: 2
  name: Wordnik Content Provider Example
  slug: wordnik-content-provider-example
- key_count: 16
  name: Wordnik Definition Example
  slug: wordnik-definition-example
- key_count: 2
  name: Wordnik Definition Search Results Example
  slug: wordnik-definition-search-results-example
- key_count: 12
  name: Wordnik Example Example
  slug: wordnik-example-example
- key_count: 2
  name: Wordnik Example Search Results Example
  slug: wordnik-example-search-results-example
- key_count: 1
  name: Wordnik Example Usage Example
  slug: wordnik-example-usage-example
- key_count: 2
  name: Wordnik Facet Example
  slug: wordnik-facet-example
- key_count: 2
  name: Wordnik Facet Value Example
  slug: wordnik-facet-value-example
- key_count: 2
  name: Wordnik Frequency Example
  slug: wordnik-frequency-example
- key_count: 5
  name: Wordnik Frequency Summary Example
  slug: wordnik-frequency-summary-example
- key_count: 2
  name: Wordnik Label Example
  slug: wordnik-label-example
- key_count: 4
  name: Wordnik Note Example
  slug: wordnik-note-example
- key_count: 3
  name: Wordnik Part Of Speech Example
  slug: wordnik-part-of-speech-example
- key_count: 7
  name: Wordnik Related Example
  slug: wordnik-related-example
- key_count: 3
  name: Wordnik Root Example
  slug: wordnik-root-example
- key_count: 11
  name: Wordnik Scored Word Example
  slug: wordnik-scored-word-example
- key_count: 1
  name: Wordnik Scrabble Score Result Example
  slug: wordnik-scrabble-score-result-example
- key_count: 6
  name: Wordnik Sentence Example
  slug: wordnik-sentence-example
- key_count: 4
  name: Wordnik Simple Definition Example
  slug: wordnik-simple-definition-example
- key_count: 4
  name: Wordnik Simple Example Example
  slug: wordnik-simple-example-example
- key_count: 1
  name: Wordnik String Value Example
  slug: wordnik-string-value-example
- key_count: 3
  name: Wordnik Syllable Example
  slug: wordnik-syllable-example
- key_count: 3
  name: Wordnik Text Pron Example
  slug: wordnik-text-pron-example
- key_count: 8
  name: Wordnik User Example
  slug: wordnik-user-example
- key_count: 11
  name: Wordnik Word List Example
  slug: wordnik-word-list-example
- key_count: 7
  name: Wordnik Word List Word Example
  slug: wordnik-word-list-word-example
- key_count: 6
  name: Wordnik Word Object Example
  slug: wordnik-word-object-example
- key_count: 12
  name: Wordnik Word Of The Day Example
  slug: wordnik-word-of-the-day-example
- key_count: 3
  name: Wordnik Word Search Result Example
  slug: wordnik-word-search-result-example
- key_count: 2
  name: Wordnik Word Search Results Example
  slug: wordnik-word-search-results-example
finops:
- name: Wordnik Finops
  service_category: Language Data
  slug: wordnik-finops
image: https://wordnik.com/img/logo-wordnik-home.png
json_schemas:
- name: ApiTokenStatus
  property_count: 6
  slug: wordnik-api-token-status
- name: AudioFile
  property_count: 14
  slug: wordnik-audio-file
- name: AudioType
  property_count: 2
  slug: wordnik-audio-type
- name: AuthenticationToken
  property_count: 3
  slug: wordnik-authentication-token
- name: Bigram
  property_count: 5
  slug: wordnik-bigram
- name: Category
  property_count: 2
  slug: wordnik-category
- name: Citation
  property_count: 2
  slug: wordnik-citation
- name: ContentProvider
  property_count: 2
  slug: wordnik-content-provider
- name: Definition
  property_count: 16
  slug: wordnik-definition
- name: DefinitionSearchResults
  property_count: 2
  slug: wordnik-definition-search-results
- name: Example
  property_count: 12
  slug: wordnik-example
- name: ExampleSearchResults
  property_count: 2
  slug: wordnik-example-search-results
- name: ExampleUsage
  property_count: 1
  slug: wordnik-example-usage
- name: Facet
  property_count: 2
  slug: wordnik-facet
- name: FacetValue
  property_count: 2
  slug: wordnik-facet-value
- name: Frequency
  property_count: 2
  slug: wordnik-frequency
- name: FrequencySummary
  property_count: 5
  slug: wordnik-frequency-summary
- name: Label
  property_count: 2
  slug: wordnik-label
- name: Note
  property_count: 4
  slug: wordnik-note
- name: PartOfSpeech
  property_count: 3
  slug: wordnik-part-of-speech
- name: Related
  property_count: 7
  slug: wordnik-related
- name: Root
  property_count: 3
  slug: wordnik-root
- name: ScoredWord
  property_count: 11
  slug: wordnik-scored-word
- name: ScrabbleScoreResult
  property_count: 1
  slug: wordnik-scrabble-score-result
- name: Sentence
  property_count: 6
  slug: wordnik-sentence
- name: SimpleDefinition
  property_count: 4
  slug: wordnik-simple-definition
- name: SimpleExample
  property_count: 4
  slug: wordnik-simple-example
- name: StringValue
  property_count: 1
  slug: wordnik-string-value
- name: Syllable
  property_count: 3
  slug: wordnik-syllable
- name: TextPron
  property_count: 3
  slug: wordnik-text-pron
- name: User
  property_count: 8
  slug: wordnik-user
- name: WordList
  property_count: 11
  slug: wordnik-word-list
- name: WordListWord
  property_count: 7
  slug: wordnik-word-list-word
- name: WordObject
  property_count: 6
  slug: wordnik-word-object
- name: WordOfTheDay
  property_count: 12
  slug: wordnik-word-of-the-day
- name: WordSearchResult
  property_count: 3
  slug: wordnik-word-search-result
- name: WordSearchResults
  property_count: 2
  slug: wordnik-word-search-results
json_structures:
- name: Wordnik Api Token Status Structure
  property_count: 6
  slug: wordnik-api-token-status-structure
- name: Wordnik Audio File Structure
  property_count: 14
  slug: wordnik-audio-file-structure
- name: Wordnik Audio Type Structure
  property_count: 2
  slug: wordnik-audio-type-structure
- name: Wordnik Authentication Token Structure
  property_count: 3
  slug: wordnik-authentication-token-structure
- name: Wordnik Bigram Structure
  property_count: 5
  slug: wordnik-bigram-structure
- name: Wordnik Category Structure
  property_count: 2
  slug: wordnik-category-structure
- name: Wordnik Citation Structure
  property_count: 2
  slug: wordnik-citation-structure
- name: Wordnik Content Provider Structure
  property_count: 2
  slug: wordnik-content-provider-structure
- name: Wordnik Definition Search Results Structure
  property_count: 2
  slug: wordnik-definition-search-results-structure
- name: Wordnik Definition Structure
  property_count: 16
  slug: wordnik-definition-structure
- name: Wordnik Example Search Results Structure
  property_count: 2
  slug: wordnik-example-search-results-structure
- name: Wordnik Example Structure
  property_count: 12
  slug: wordnik-example-structure
- name: Wordnik Example Usage Structure
  property_count: 1
  slug: wordnik-example-usage-structure
- name: Wordnik Facet Structure
  property_count: 2
  slug: wordnik-facet-structure
- name: Wordnik Facet Value Structure
  property_count: 2
  slug: wordnik-facet-value-structure
- name: Wordnik Frequency Structure
  property_count: 2
  slug: wordnik-frequency-structure
- name: Wordnik Frequency Summary Structure
  property_count: 5
  slug: wordnik-frequency-summary-structure
- name: Wordnik Label Structure
  property_count: 2
  slug: wordnik-label-structure
- name: Wordnik Note Structure
  property_count: 4
  slug: wordnik-note-structure
- name: Wordnik Part Of Speech Structure
  property_count: 3
  slug: wordnik-part-of-speech-structure
- name: Wordnik Related Structure
  property_count: 7
  slug: wordnik-related-structure
- name: Wordnik Root Structure
  property_count: 3
  slug: wordnik-root-structure
- name: Wordnik Scored Word Structure
  property_count: 11
  slug: wordnik-scored-word-structure
- name: Wordnik Scrabble Score Result Structure
  property_count: 1
  slug: wordnik-scrabble-score-result-structure
- name: Wordnik Sentence Structure
  property_count: 6
  slug: wordnik-sentence-structure
- name: Wordnik Simple Definition Structure
  property_count: 4
  slug: wordnik-simple-definition-structure
- name: Wordnik Simple Example Structure
  property_count: 4
  slug: wordnik-simple-example-structure
- name: Wordnik String Value Structure
  property_count: 1
  slug: wordnik-string-value-structure
- name: Wordnik Syllable Structure
  property_count: 3
  slug: wordnik-syllable-structure
- name: Wordnik Text Pron Structure
  property_count: 3
  slug: wordnik-text-pron-structure
- name: Wordnik User Structure
  property_count: 8
  slug: wordnik-user-structure
- name: Wordnik Word List Structure
  property_count: 11
  slug: wordnik-word-list-structure
- name: Wordnik Word List Word Structure
  property_count: 7
  slug: wordnik-word-list-word-structure
- name: Wordnik Word Object Structure
  property_count: 6
  slug: wordnik-word-object-structure
- name: Wordnik Word Of The Day Structure
  property_count: 12
  slug: wordnik-word-of-the-day-structure
- name: Wordnik Word Search Result Structure
  property_count: 3
  slug: wordnik-word-search-result-structure
- name: Wordnik Word Search Results Structure
  property_count: 2
  slug: wordnik-word-search-results-structure
jsonld:
- class_count: 37
  name: Wordnik Context
  property_count: 116
  slug: wordnik-context
layout: provider
modified: '2026-05-29'
name: Wordnik
nav: Providers
network: true
overview: 'Wordnik publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Word API, Word List API, and 2 more. Tagged areas include Dictionaries, Dictionary, Word Data, English, and Lexicography.


  The Wordnik catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wordnik''s developer surface includes authentication, documentation, pricing, getting-started guide, signup flow, engineering blog, support, and 17 more developer resources.'
plans:
- name: Wordnik Plans Pricing
  plan_count: 4
  slug: wordnik-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Wordnik Rate Limits
  slug: wordnik-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wordnik API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wordnik-jsonschema-spectral-rules
- effective_rule_count: 45
  extends: []
  name: Wordnik API Rules
  rule_count: 45
  severity_counts:
    error: 9
    hint: 0
    info: 6
    warn: 30
  slug: wordnik-rules
score:
  band: strong
  composite: 57.1
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 28.8
    contract_quality: 61.0
    developer_ergonomics: 45.2
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 50.0
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wordnik/refs/heads/main/screenshots/wordnik-2026-06-20T201543.png
security:
- kind: authentication
  name: Wordnik Authentication
  slug: wordnik-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Wordnik Domain Security
  slug: wordnik-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: wordnik
tags:
- Dictionaries
- Dictionary
- Word Data
- English
- Lexicography
- Public APIs
website: https://wordnik.com
---
