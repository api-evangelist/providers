---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Datamuse Agentic Access
  operation_count: 2
  slug: datamuse-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Autocomplete suggestions with spelling correction and semantic fallback.
  name: Datamuse Suggestions API
  slug: datamuse-suggestions-api
- description: Word-finding queries combining semantic, phonetic, orthographic, and vocabulary constraints.
  name: Datamuse Words API
  slug: datamuse-words-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Datamuse Suggestions API
  slug: open-datamuse-suggestions-api
- collection_type: open
  name: Datamuse Suggestions Words API
  slug: open-datamuse-words-api
- collection_type: open
  name: Datamuse API
  slug: open-datamuse
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datamuse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datamuse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datamuse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.datamuse.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.datamuse.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datamuse.com/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datamuse.com/api/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datamuse.com/api/
- group: operate
  title: ''
  type: Support
  url: https://www.datamuse.com/api/
- group: design
  title: ''
  type: SpectralRules
  url: rules/datamuse-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/datamuse-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/datamuse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datamuse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datamuse-finops.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sjblair/Datamuse4J
- group: build
  title: ''
  type: SDKs
  url: https://github.com/gmarmstrong/python-datamuse
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ansteh/datamuse
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ezefranca/datamuse-swift
- group: build
  title: ''
  type: SDKs
  url: https://github.com/owenvoke/datamuse-php-api-wrapper
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kostaspt/go-datamuse
- group: build
  title: ''
  type: SDKs
  url: https://github.com/slogemann1/datamuse-api-wrapper
- group: build
  title: ''
  type: SDKs
  url: https://github.com/benhess02/DatamuseDotNet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mosegontar/rubymuse
- group: build
  title: ''
  type: Tools
  url: https://github.com/lacausecrypto/datamuse-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/pipeworx-io/mcp-datamuse
- group: build
  title: ''
  type: Tools
  url: https://github.com/bhayanak/datamuse-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/pipeworx-io/mcp-words
- group: build
  title: ''
  type: Tools
  url: https://github.com/Eyalm321/multilingual-dictionary-mcp
created: '2026-05-28'
description: Datamuse operates a word-finding query engine and lexical search service for developers, educators, and creative-writing applications. The Datamuse API exposes a /words endpoint that finds words matching a rich combination of semantic, phonetic, orthographic, and vocabulary constraints (means-like, sounds-like, spelled-like, synonyms, antonyms, hypernyms, meronyms, triggers, rhymes, homophones, and more) plus a /sug autocomplete endpoint. Free for non-commercial use up to 100,000 requests per day with no API key required; commercial use, custom vocabularies, and higher rate limits are available via a paid commercial agreement. Datamuse also runs OneLook, OneLook Thesaurus, RhymeZone, Rimar.io, and CivicSearch — consumer-facing word search tools built on the same lexical infrastructure.
examples:
- key_count: 3
  name: Datamuse Getsuggestions Example
  slug: datamuse-getsuggestions-example
- key_count: 3
  name: Datamuse Getwords Example
  slug: datamuse-getwords-example
features:
- description: Reverse-dictionary semantic constraint finding words whose meaning matches an input string of any length.
  name: Means Like (ml)
- description: Phonetic constraint returning words pronounced similarly to a given input using a text-to-phonemes algorithm.
  name: Sounds Like (sl)
- description: Orthographic constraint with wildcard pattern matching (* for any chars, ? for a single char).
  name: Spelled Like (sp)
- description: Twelve lexical relations including synonyms, antonyms, hypernyms, hyponyms, holonyms, meronyms, triggers, frequent followers/predecessors, rhymes, near-rhymes, homophones, and consonant matches.
  name: Predefined Relations (rel_*)
- description: Topics, left-context (lc), and right-context (rc) parameters skew results toward a document theme or surrounding words.
  name: Context Ranking
- description: Optional metadata flags add definitions, parts of speech, syllable counts, pronunciations, and corpus frequency to each word.
  name: Lexical Metadata (md)
- description: Default Arpabet pronunciations or IPA via the ipa flag, drawing on the CMU Pronouncing Dictionary.
  name: Pronunciation Formats
- description: Default English (550k terms) and Spanish (500k terms) vocabularies; custom domain vocabularies available on request.
  name: Multilingual Vocabularies
- description: Intelligent prefix suggestions with spelling correction and semantic fallback when exact matches are unavailable.
  name: Autocomplete (/sug)
- description: Free non-commercial use up to 100,000 requests per day without an account or API token; HTTPS and HTTP both supported.
  name: No API Key Required
- description: Prepends the result list with a record describing the query string, useful for one-shot word-metadata lookups.
  name: Query Echo (qe)
finops:
- name: Datamuse Finops
  service_category: ''
  slug: datamuse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datamuse.png
integrations:
- description: Datamuse's flagship word search engine indexing 10M+ words across 1000+ dictionaries; built on the same backend.
  name: OneLook
- description: Reverse-dictionary and thesaurus product available on web, as a Google Docs add-on, and as an iOS/Mac app.
  name: OneLook Thesaurus
- description: Rhyming dictionary and writing tool partnered with Merriam-Webster, available on web and mobile.
  name: RhymeZone
- description: Spanish-language rhyming dictionary and thesaurus powered by Datamuse's Spanish vocabulary.
  name: Rimar.io
- description: Local government meeting search engine covering 700+ jurisdictions across the US and Canada.
  name: CivicSearch
- description: Princeton lexical database supplying synonyms, antonyms, hypernyms, hyponyms, holonyms, and meronyms.
  name: WordNet 3.0
- description: Source for Arpabet pronunciations and the basis for phonetic constraints (sl, rel_rhy, rel_hom, rel_cns).
  name: CMU Pronouncing Dictionary
- description: Corpus underpinning frequency scores and the rel_jja, rel_jjb, rel_bga, rel_bgb statistical relations.
  name: Google Books Ngrams
- description: Source of definitions returned via the md=d metadata flag.
  name: Wiktionary
- description: Corpus and embedding sources contributing to means-like and trigger relations.
  name: word2vec / Paraphrase Database
- description: Community plugin embedding Datamuse-powered thesaurus and reverse-dictionary directly into Obsidian.
  name: Obsidian Wordy Plugin
- description: Multiple community MCP servers (lacausecrypto/datamuse-mcp, pipeworx-io/mcp-datamuse, bhayanak/datamuse-mcp-server) expose the API to LLM agents.
  name: Model Context Protocol Servers
json_schemas:
- name: Datamuse Suggestion
  property_count: 2
  slug: datamuse-suggestion
- name: Datamuse Word
  property_count: 6
  slug: datamuse-word
json_structures:
- name: Datamuse Suggestion Structure
  property_count: 0
  slug: datamuse-suggestion-structure
- name: Datamuse Word Structure
  property_count: 0
  slug: datamuse-word-structure
jsonld:
- class_count: 14
  name: Datamuse Context
  property_count: 6
  slug: datamuse-context
layout: provider
modified: '2026-05-29'
name: Datamuse
nav: Providers
network: true
overview: 'Datamuse publishes 2 APIs on the [APIs.io](https://apis.io/) network: Suggestions API and Words API. Tagged areas include Word Finding, Lexical Search, Natural Language, Vocabulary, and Synonyms.


  The Datamuse catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Datamuse''s developer surface includes documentation, API reference, pricing, support, tooling, and 24 more developer resources.'
plans:
- name: Datamuse Plans Pricing
  plan_count: 2
  slug: datamuse-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 0
  name: Datamuse Rate Limits
  slug: datamuse-rate-limits
rules:
- name: Datamuse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: datamuse-jsonschema-spectral-rules
- name: Datamuse API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 6
  slug: datamuse-rules
score:
  band: developing
  composite: 52.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.9
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 0.0
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datamuse/refs/heads/main/screenshots/datamuse-2026-06-20T175644.png
security:
- kind: domain-security
  name: Datamuse Domain Security
  slug: datamuse-domain-security
  summary_line: TLSv1.2 · DMARC
slug: datamuse
solutions:
- description: Up to 100,000 requests per day with no API key, no signup, suitable for prototypes, hobby projects, research, and non-commercial education.
  name: Free Non-Commercial Tier
- description: Custom contract for production traffic in customer-facing applications, higher quotas, custom vocabularies, and SLA — pricing on request.
  name: Commercial Plan
- description: Domain-specific term lists (medical, legal, gaming, internal jargon) hosted on Datamuse infrastructure with all standard relations.
  name: Custom Vocabulary Hosting
tags:
- Word Finding
- Lexical Search
- Natural Language
- Vocabulary
- Synonyms
- Antonyms
- Rhymes
- Phonetics
- Semantic Search
- Reverse Dictionary
- Autocomplete
- Wordplay
- Creative Writing
- Vocabulary Apps
- Word Games
- Linguistics
- Open Source Projects
- Public APIs
use_cases:
- description: Power flashcards, quizzes, and language-learning apps with synonyms, antonyms, and related-word lookups.
  name: Vocabulary Building Apps
- description: Drive rhyme finders, thesaurus add-ins, and reverse-dictionary lookups for poetry, songwriting, and copywriting.
  name: Creative Writing Tools
- description: Generate clues, fill patterns with sp wildcards, and validate word lists for crosswords, hangman, and word ladders.
  name: Word Games and Puzzles
- description: Provide intelligent prefix suggestions with spelling correction in search bars and form fields.
  name: Autocomplete and Type-Ahead
- description: Add definitions, syllable counts, and pronunciations to reading apps, ESL tools, and accessibility software.
  name: Educational Software
- description: Expand a user's search terms with semantically related words to improve recall in document or product search.
  name: Search Query Expansion
- description: Look up word relations, frequencies, and pronunciations as features for downstream NLP pipelines.
  name: NLP Pre-Processing
- description: Combine sounds-like, means-like, and spelled-like constraints to brainstorm brand, domain, or product names.
  name: Brand and Product Naming
website: https://www.datamuse.com/
---
