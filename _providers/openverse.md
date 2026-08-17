---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Openverse Agentic Access
  operation_count: 17
  slug: openverse-agentic-access
  summary_line: 17 operations · 4 acting
api_count: 3
apis:
- description: These are endpoints pertaining to audio files.
  name: Openverse audio API
  slug: openverse-audio-api
- description: Openverse provides free and open access to the Openverse API to anonymous and registered users. [Refer to the API documentation site for information on how to register](https://api.openverse.org/v1/#t
  name: Openverse auth API
  slug: openverse-auth-api
- description: These are endpoints pertaining to images.
  name: Openverse images API
  slug: openverse-images-api
artifact_total: 92
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Openverse audio API
  slug: open-openverse-audio-api
- collection_type: open
  name: Openverse audio auth API
  slug: open-openverse-auth-api
- collection_type: open
  name: Openverse audio images API
  slug: open-openverse-images-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/WordPress/openverse/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openverse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openverse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openverse-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://make.wordpress.org/openverse/feed/
created: '2026-06-13'
description: Openverse is a search engine providing programmatic access to the world's largest openly-licensed media catalog, covering 800M+ images and audio tracks from cultural institutions, museums, and creative commons sources including Flickr, Wikimedia Commons, iNaturalist, Europeana, Freesound, Jamendo, and more. Built by WordPress/Automattic under Creative Commons licensing principles.
examples:
- key_count: 30
  name: Audio_Detail_200
  slug: audio_detail_200
- key_count: 1
  name: Audio_Detail_401
  slug: audio_detail_401
- key_count: 1
  name: Audio_Detail_404
  slug: audio_detail_404
- key_count: 6
  name: Audio_Related_200
  slug: audio_related_200
- key_count: 1
  name: Audio_Related_401
  slug: audio_related_401
- key_count: 1
  name: Audio_Related_404
  slug: audio_related_404
- key_count: 3
  name: Audio_Report_201
  slug: audio_report_201
- key_count: 1
  name: Audio_Report_400
  slug: audio_report_400
- key_count: 1
  name: Audio_Report_401
  slug: audio_report_401
- key_count: 1
  name: Audio_Report_404
  slug: audio_report_404
- key_count: 6
  name: Audio_Search_200
  slug: audio_search_200
- key_count: 3
  name: Audio_Search_400
  slug: audio_search_400
- key_count: 1
  name: Audio_Search_401
  slug: audio_search_401
- key_count: 1
  name: Audio_Stats_401
  slug: audio_stats_401
- key_count: 4
  name: Audio_Thumb_401_Stub
  slug: audio_thumb_401_stub
- key_count: 4
  name: Audio_Thumb_404_Stub
  slug: audio_thumb_404_stub
- key_count: 2
  name: Audio_Waveform_200
  slug: audio_waveform_200
- key_count: 1
  name: Audio_Waveform_401
  slug: audio_waveform_401
- key_count: 1
  name: Audio_Waveform_404
  slug: audio_waveform_404
- key_count: 25
  name: Images_Detail_200
  slug: images_detail_200
- key_count: 1
  name: Images_Detail_401
  slug: images_detail_401
- key_count: 1
  name: Images_Detail_404
  slug: images_detail_404
- key_count: 8
  name: Images_Oembed_200
  slug: images_oembed_200
- key_count: 1
  name: Images_Oembed_400
  slug: images_oembed_400
- key_count: 1
  name: Images_Oembed_401
  slug: images_oembed_401
- key_count: 1
  name: Images_Oembed_404
  slug: images_oembed_404
- key_count: 6
  name: Images_Related_200
  slug: images_related_200
- key_count: 1
  name: Images_Related_401
  slug: images_related_401
- key_count: 1
  name: Images_Related_404
  slug: images_related_404
- key_count: 3
  name: Images_Report_201
  slug: images_report_201
- key_count: 1
  name: Images_Report_400
  slug: images_report_400
- key_count: 1
  name: Images_Report_401
  slug: images_report_401
- key_count: 1
  name: Images_Report_404
  slug: images_report_404
- key_count: 6
  name: Images_Search_200
  slug: images_search_200
- key_count: 3
  name: Images_Search_400
  slug: images_search_400
- key_count: 1
  name: Images_Search_401
  slug: images_search_401
- key_count: 1
  name: Images_Stats_401
  slug: images_stats_401
- key_count: 4
  name: Images_Thumb_401_Stub
  slug: images_thumb_401_stub
- key_count: 4
  name: Images_Thumb_404_Stub
  slug: images_thumb_404_stub
- key_count: 3
  name: Key_Info_200
  slug: key_info_200
- key_count: 1
  name: Key_Info_401
  slug: key_info_401
- key_count: 4
  name: Key_Info_429_Stub
  slug: key_info_429_stub
- key_count: 1
  name: Key_Info_500
  slug: key_info_500
- key_count: 3
  name: Register_201
  slug: register_201
- key_count: 1
  name: Register_400
  slug: register_400
- key_count: 4
  name: Register_401_Stub
  slug: register_401_stub
- key_count: 4
  name: Register_429_Stub
  slug: register_429_stub
- key_count: 4
  name: Token_200
  slug: token_200
- key_count: 4
  name: Token_400_Stub
  slug: token_400_stub
- key_count: 1
  name: Token_401
  slug: token_401
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://openverse.org/openverse-logo.svg
json_schemas:
- name: APIException
  property_count: 1
  slug: apiexception
- name: Audio
  property_count: 29
  slug: audio
- name: AudioAltFile
  property_count: 5
  slug: audioaltfile
- name: AudioReportRequest
  property_count: 3
  slug: audioreportrequest
- name: AudioSet
  property_count: 7
  slug: audioset
- name: AudioWaveform
  property_count: 2
  slug: audiowaveform
- name: AuthenticationFailed
  property_count: 1
  slug: authenticationfailed
- name: GrantTypeEnum
  property_count: 0
  slug: granttypeenum
- name: Image
  property_count: 24
  slug: image
- name: ImageReportRequest
  property_count: 3
  slug: imagereportrequest
- name: NotAuthenticated
  property_count: 1
  slug: notauthenticated
- name: NotFound
  property_count: 1
  slug: notfound
- name: OAuth2Application
  property_count: 4
  slug: oauth2application
- name: OAuth2KeyInfo
  property_count: 4
  slug: oauth2keyinfo
- name: OAuth2Registration
  property_count: 3
  slug: oauth2registration
- name: OAuth2Token
  property_count: 4
  slug: oauth2token
- name: OAuth2TokenRequest
  property_count: 3
  slug: oauth2tokenrequest
- name: Oembed
  property_count: 8
  slug: oembed
- name: PaginatedAudioList
  property_count: 6
  slug: paginatedaudiolist
- name: PaginatedImageList
  property_count: 6
  slug: paginatedimagelist
- name: ReasonEnum
  property_count: 0
  slug: reasonenum
- name: Source
  property_count: 5
  slug: source
- name: Tag
  property_count: 3
  slug: tag
- name: TypeEnum
  property_count: 0
  slug: typeenum
- name: ValidationError
  property_count: 1
  slug: validationerror
- name: VersionEnum
  property_count: 0
  slug: versionenum
jsonld:
- class_count: 30
  name: context Context
  property_count: 9
  slug: context
- class_count: 0
  name: Openverse Context
  property_count: 0
  slug: openverse
layout: provider
modified: '2026-06-13'
name: Openverse
nav: Providers
network: true
overview: 'Openverse publishes 3 APIs on the [APIs.io](https://apis.io/) network: audio API, auth API, and images API. Tagged areas include Images, Audio, Creative Commons, Open Media, and Search.


  The Openverse catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Openverse''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 89
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Openverse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openverse-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.5
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openverse/refs/heads/main/screenshots/openverse-2026-06-20T191047.png
security:
- kind: authentication
  name: Openverse Authentication
  slug: openverse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openverse Domain Security
  slug: openverse-domain-security
  summary_line: TLSv1.3
slug: openverse
tags:
- Images
- Audio
- Creative Commons
- Open Media
- Search
- Open Data
- Cultural Heritage
- Museums
---
