---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Words Agentic Access
  operation_count: 30
  slug: words-agentic-access
  summary_line: 30 operations
api_count: 9
apis:
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Category, Region, and Domain-Usage Relationships.
  name: Words API Categories API
  slug: words-categories-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Sense-level Definitions Grouped by Part of Speech.
  name: Words API Definitions API
  slug: words-definitions-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Real-world Example Sentences for Each Sense.
  name: Words API Examples API
  slug: words-examples-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Corpus-derived Frequency Statistics (Zipf, perMillion, diversity).
  name: Words API Frequency API
  slug: words-frequency-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Lexical Hierarchies — typeOf, hasTypes, partOf, hasParts, instances.
  name: Words API Hierarchy API
  slug: words-hierarchy-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Pronunciation (IPA), Syllables, and Rhymes.
  name: Words API Phonetics API
  slug: words-phonetics-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Search and Random Word Discovery Endpoint.
  name: Words API Search API
  slug: words-search-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Synonyms, Antonyms, and Similar Word Relationships.
  name: Words API Thesaurus API
  slug: words-thesaurus-api
- baseURL: https://wordsapiv1.p.rapidapi.com
  baseurl_source: declared
  description: Words API Lookup a Word and Retrieve Its Full Lexical Entry.
  name: Words API Word API
  slug: words-word-api
artifact_total: 164
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Words Categories API
  slug: open-words-categories-api
- collection_type: open
  name: Words Categories Definitions API
  slug: open-words-definitions-api
- collection_type: open
  name: Words Categories Examples API
  slug: open-words-examples-api
- collection_type: open
  name: Words Categories Frequency API
  slug: open-words-frequency-api
- collection_type: open
  name: Words Categories Hierarchy API
  slug: open-words-hierarchy-api
- collection_type: open
  name: Words Categories Phonetics API
  slug: open-words-phonetics-api
- collection_type: open
  name: Words Categories Search API
  slug: open-words-search-api
- collection_type: open
  name: Words Categories Thesaurus API
  slug: open-words-thesaurus-api
- collection_type: open
  name: Words Categories Word API
  slug: open-words-word-api
- collection_type: open
  name: Words API
  slug: open-words
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/WordsAPI/wordfrequencies/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/words-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/words-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/words-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wordsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wordsapi.com/docs/
- group: start
  title: ''
  type: Signup
  url: https://rapidapi.com/dpventures/api/wordsapi
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/dpventures/api/wordsapi/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.wordsapi.com/
- group: operate
  title: ''
  type: Contact
  url: mailto:support@wordsapi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WordsAPI
- group: build
  title: Word Frequencies Dataset
  type: GitHubRepository
  url: https://github.com/WordsAPI/wordfrequencies
- group: other
  title: RapidAPI Listing
  type: Marketplace
  url: https://rapidapi.com/dpventures/api/wordsapi
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/words-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/words-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/words-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/words-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/words-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/words-context.jsonld
created: '2026-05-28'
description: Words API is a RESTful English-language API that provides definitions, synonyms, antonyms, related words, syllables, pronunciation (IPA), rhymes, frequency, and hierarchical lexical relationships (typeOf, hasTypes, partOf, hasParts, memberOf, similarTo, also, entails, inCategory, inRegion, pertainsTo, etc.) for more than 150,000 English words. Distributed and metered through the RapidAPI marketplace.
examples:
- key_count: 2
  name: Words Also Response Example
  slug: words-also-response-example
- key_count: 2
  name: Words Antonyms Response Example
  slug: words-antonyms-response-example
- key_count: 2
  name: Words Definition Entry Example
  slug: words-definition-entry-example
- key_count: 2
  name: Words Definitions Response Example
  slug: words-definitions-response-example
- key_count: 2
  name: Words Entails Response Example
  slug: words-entails-response-example
- key_count: 2
  name: Words Examples Response Example
  slug: words-examples-response-example
- key_count: 3
  name: Words Frequency Example
  slug: words-frequency-example
- key_count: 0
  name: Words Frequency Response Example
  slug: words-frequency-response-example
- key_count: 2
  name: Words Has Categories Response Example
  slug: words-has-categories-response-example
- key_count: 2
  name: Words Has Members Response Example
  slug: words-has-members-response-example
- key_count: 2
  name: Words Has Parts Response Example
  slug: words-has-parts-response-example
- key_count: 2
  name: Words Has Substances Response Example
  slug: words-has-substances-response-example
- key_count: 2
  name: Words Has Types Response Example
  slug: words-has-types-response-example
- key_count: 2
  name: Words Has Usages Response Example
  slug: words-has-usages-response-example
- key_count: 2
  name: Words In Category Response Example
  slug: words-in-category-response-example
- key_count: 2
  name: Words In Region Response Example
  slug: words-in-region-response-example
- key_count: 2
  name: Words Instance Of Response Example
  slug: words-instance-of-response-example
- key_count: 2
  name: Words Instances Response Example
  slug: words-instances-response-example
- key_count: 2
  name: Words Member Of Response Example
  slug: words-member-of-response-example
- key_count: 2
  name: Words Part Of Response Example
  slug: words-part-of-response-example
- key_count: 2
  name: Words Pertains To Response Example
  slug: words-pertains-to-response-example
- key_count: 5
  name: Words Pronunciation Example
  slug: words-pronunciation-example
- key_count: 2
  name: Words Pronunciation Response Example
  slug: words-pronunciation-response-example
- key_count: 2
  name: Words Region Of Response Example
  slug: words-region-of-response-example
- key_count: 25
  name: Words Result Example
  slug: words-result-example
- key_count: 2
  name: Words Rhymes Response Example
  slug: words-rhymes-response-example
- key_count: 3
  name: Words Search Response Example
  slug: words-search-response-example
- key_count: 3
  name: Words Search Results Meta Example
  slug: words-search-results-meta-example
- key_count: 2
  name: Words Similar To Response Example
  slug: words-similar-to-response-example
- key_count: 2
  name: Words Substance Of Response Example
  slug: words-substance-of-response-example
- key_count: 2
  name: Words Syllables Example
  slug: words-syllables-example
- key_count: 3
  name: Words Syllables Response Example
  slug: words-syllables-response-example
- key_count: 2
  name: Words Synonyms Response Example
  slug: words-synonyms-response-example
- key_count: 2
  name: Words Type Of Response Example
  slug: words-type-of-response-example
- key_count: 2
  name: Words Usage Of Response Example
  slug: words-usage-of-response-example
- key_count: 5
  name: Words Word Entry Example
  slug: words-word-entry-example
features:
- description: Definitions, syllables, pronunciation, and lexical relationships across more than 150,000 English words.
  name: 150,000+ English Words
- description: Per-sense definitions grouped by part of speech (noun, verb, adjective, adverb).
  name: Definitions and Parts of Speech
- description: Interchangeable and opposite-meaning words for each sense of a word.
  name: Thesaurus (Synonyms and Antonyms)
- description: typeOf, hasTypes, partOf, hasParts, instanceOf, hasInstances, memberOf, hasMembers, substanceOf, hasSubstances, inCategory, hasCategories relationships.
  name: Lexical Hierarchies
- description: International Phonetic Alphabet pronunciation, optionally split per part of speech.
  name: Pronunciation in IPA
- description: Syllable count and the ordered list of syllables for each word.
  name: Syllable Breakdown
- description: Lists of rhyming words, distinguished by pronunciation variant where pronunciations differ.
  name: Rhymes
- description: Zipf frequency (1–7), per-million occurrence rate, and corpus diversity score derived from large English subtitle corpora.
  name: Frequency Data
- description: Sample sentences illustrating real usage for each sense.
  name: Examples
- description: inRegion, regionOf, inCategory, hasCategories, usageOf, hasUsages relationships connect words to dialects and subject domains.
  name: Regional and Domain Usage
- description: /words search endpoint supports letter count, letter pattern, phoneme count, IPA pattern, part of speech, and random selection.
  name: Random and Filtered Word Search
finops:
- name: Words Finops
  service_category: Linguistic Data & Lexical Services
  slug: words-finops
image: https://www.wordsapi.com/img/logo.png
integrations:
- description: Words API is distributed, authenticated, and metered through the RapidAPI marketplace.
  name: RapidAPI
- description: Lexical relationships (typeOf, hasParts, memberOf, etc.) follow the WordNet relational model.
  name: WordNet
- description: Frequency data is derived from large English movie and television subtitle corpora (see WordsAPI/wordfrequencies on GitHub).
  name: Subtitle Corpora
json_schemas:
- name: AlsoResponse
  property_count: 2
  slug: words-also-response
- name: AntonymsResponse
  property_count: 2
  slug: words-antonyms-response
- name: DefinitionEntry
  property_count: 2
  slug: words-definition-entry
- name: DefinitionsResponse
  property_count: 2
  slug: words-definitions-response
- name: EntailsResponse
  property_count: 2
  slug: words-entails-response
- name: ExamplesResponse
  property_count: 2
  slug: words-examples-response
- name: FrequencyResponse
  property_count: 0
  slug: words-frequency-response
- name: Frequency
  property_count: 3
  slug: words-frequency
- name: HasCategoriesResponse
  property_count: 2
  slug: words-has-categories-response
- name: HasMembersResponse
  property_count: 2
  slug: words-has-members-response
- name: HasPartsResponse
  property_count: 2
  slug: words-has-parts-response
- name: HasSubstancesResponse
  property_count: 2
  slug: words-has-substances-response
- name: HasTypesResponse
  property_count: 2
  slug: words-has-types-response
- name: HasUsagesResponse
  property_count: 2
  slug: words-has-usages-response
- name: InCategoryResponse
  property_count: 2
  slug: words-in-category-response
- name: InRegionResponse
  property_count: 2
  slug: words-in-region-response
- name: InstanceOfResponse
  property_count: 2
  slug: words-instance-of-response
- name: InstancesResponse
  property_count: 2
  slug: words-instances-response
- name: MemberOfResponse
  property_count: 2
  slug: words-member-of-response
- name: PartOfResponse
  property_count: 2
  slug: words-part-of-response
- name: PertainsToResponse
  property_count: 2
  slug: words-pertains-to-response
- name: PronunciationResponse
  property_count: 2
  slug: words-pronunciation-response
- name: Pronunciation
  property_count: 5
  slug: words-pronunciation
- name: RegionOfResponse
  property_count: 2
  slug: words-region-of-response
- name: Result
  property_count: 25
  slug: words-result
- name: RhymesResponse
  property_count: 2
  slug: words-rhymes-response
- name: SearchResponse
  property_count: 3
  slug: words-search-response
- name: SearchResultsMeta
  property_count: 3
  slug: words-search-results-meta
- name: SimilarToResponse
  property_count: 2
  slug: words-similar-to-response
- name: SubstanceOfResponse
  property_count: 2
  slug: words-substance-of-response
- name: SyllablesResponse
  property_count: 3
  slug: words-syllables-response
- name: Syllables
  property_count: 2
  slug: words-syllables
- name: SynonymsResponse
  property_count: 2
  slug: words-synonyms-response
- name: TypeOfResponse
  property_count: 2
  slug: words-type-of-response
- name: UsageOfResponse
  property_count: 2
  slug: words-usage-of-response
- name: WordEntry
  property_count: 5
  slug: words-word-entry
json_structures:
- name: Words Also Response Structure
  property_count: 2
  slug: words-also-response-structure
- name: Words Antonyms Response Structure
  property_count: 2
  slug: words-antonyms-response-structure
- name: Words Definition Entry Structure
  property_count: 2
  slug: words-definition-entry-structure
- name: Words Definitions Response Structure
  property_count: 2
  slug: words-definitions-response-structure
- name: Words Entails Response Structure
  property_count: 2
  slug: words-entails-response-structure
- name: Words Examples Response Structure
  property_count: 2
  slug: words-examples-response-structure
- name: Words Frequency Response Structure
  property_count: 0
  slug: words-frequency-response-structure
- name: Words Frequency Structure
  property_count: 3
  slug: words-frequency-structure
- name: Words Has Categories Response Structure
  property_count: 2
  slug: words-has-categories-response-structure
- name: Words Has Members Response Structure
  property_count: 2
  slug: words-has-members-response-structure
- name: Words Has Parts Response Structure
  property_count: 2
  slug: words-has-parts-response-structure
- name: Words Has Substances Response Structure
  property_count: 2
  slug: words-has-substances-response-structure
- name: Words Has Types Response Structure
  property_count: 2
  slug: words-has-types-response-structure
- name: Words Has Usages Response Structure
  property_count: 2
  slug: words-has-usages-response-structure
- name: Words In Category Response Structure
  property_count: 2
  slug: words-in-category-response-structure
- name: Words In Region Response Structure
  property_count: 2
  slug: words-in-region-response-structure
- name: Words Instance Of Response Structure
  property_count: 2
  slug: words-instance-of-response-structure
- name: Words Instances Response Structure
  property_count: 2
  slug: words-instances-response-structure
- name: Words Member Of Response Structure
  property_count: 2
  slug: words-member-of-response-structure
- name: Words Part Of Response Structure
  property_count: 2
  slug: words-part-of-response-structure
- name: Words Pertains To Response Structure
  property_count: 2
  slug: words-pertains-to-response-structure
- name: Words Pronunciation Response Structure
  property_count: 2
  slug: words-pronunciation-response-structure
- name: Words Pronunciation Structure
  property_count: 5
  slug: words-pronunciation-structure
- name: Words Region Of Response Structure
  property_count: 2
  slug: words-region-of-response-structure
- name: Words Result Structure
  property_count: 25
  slug: words-result-structure
- name: Words Rhymes Response Structure
  property_count: 2
  slug: words-rhymes-response-structure
- name: Words Search Response Structure
  property_count: 3
  slug: words-search-response-structure
- name: Words Search Results Meta Structure
  property_count: 3
  slug: words-search-results-meta-structure
- name: Words Similar To Response Structure
  property_count: 2
  slug: words-similar-to-response-structure
- name: Words Substance Of Response Structure
  property_count: 2
  slug: words-substance-of-response-structure
- name: Words Syllables Response Structure
  property_count: 3
  slug: words-syllables-response-structure
- name: Words Syllables Structure
  property_count: 2
  slug: words-syllables-structure
- name: Words Synonyms Response Structure
  property_count: 2
  slug: words-synonyms-response-structure
- name: Words Type Of Response Structure
  property_count: 2
  slug: words-type-of-response-structure
- name: Words Usage Of Response Structure
  property_count: 2
  slug: words-usage-of-response-structure
- name: Words Word Entry Structure
  property_count: 5
  slug: words-word-entry-structure
jsonld:
- class_count: 36
  name: Words Context
  property_count: 48
  slug: words-context
layout: provider
modified: '2026-05-30'
name: Words API
nav: Providers
network: true
overview: 'Words API publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Definitions API, Examples API, and 6 more. Tagged areas include Dictionaries, Linguistics, English, Thesaurus, and Lexical Data.


  The Words API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Words API''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Words Plans Pricing
  plan_count: 5
  slug: words-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Words Rate Limits
  slug: words-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Words API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: words-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Words API API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 18
  slug: words-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 97.5
    catalog_earned_first_party: 0.0
    catalog_gap: 17.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 28.8
    contract_quality: 31.6
    developer_ergonomics: 31.0
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/words/refs/heads/main/screenshots/words-2026-06-20T201547.png
security:
- kind: authentication
  name: Words Authentication
  slug: words-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Words Domain Security
  slug: words-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: words
solutions:
- description: 2,500 requests per day at no charge for prototyping, students, and small projects.
  name: Free Tier
- description: $10 / month, 25,000 requests per day for production applications and games.
  name: Pro
- description: $49 / month, 250,000 requests per day for high-volume consumer applications.
  name: Ultra
- description: $89 / month, 500,000 requests per day for very high-volume production workloads.
  name: Mega
- description: One-time $629 purchase of the full Words API dataset for local hosting.
  name: Data Purchase
tags:
- Dictionaries
- Linguistics
- English
- Thesaurus
- Lexical Data
- Public APIs
use_cases:
- description: Power dictionary, thesaurus, and "word of the day" applications with definitions, synonyms, and related words.
  name: Dictionary and Thesaurus Applications
- description: Drive crossword, Scrabble-style, and anagram games with filtered word search, rhymes, and difficulty-tunable random word selection.
  name: Word Games and Puzzles
- description: Build grammar, style, and writing assistants that suggest synonyms, antonyms, and frequency-aware alternatives.
  name: Writing and Editing Tools
- description: Provide IPA pronunciation, syllable splits, frequency, and example sentences for ESL and vocabulary-building apps.
  name: Language Learning and Education
- description: Enrich downstream NLP pipelines with hypernyms, hyponyms, meronyms, and domain labels for entity expansion.
  name: NLP and Text Enrichment
- description: Use IPA pronunciation and syllable data for speech synthesis, ASR vocabulary tuning, and pronunciation coaching.
  name: Voice and Speech Applications
- description: Disambiguate user input by mapping words to their senses, hypernyms, and categories at runtime.
  name: Chatbots and Conversational Agents
- description: Drive paraphrasing and content-variation engines with synonym, similar-to, and pertains-to relationships.
  name: Content Generation and Rewriting
website: https://www.wordsapi.com/
---
