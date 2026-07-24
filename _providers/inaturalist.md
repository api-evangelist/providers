---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Inaturalist Agentic Access
  operation_count: 105
  slug: inaturalist-agentic-access
  summary_line: 105 operations · 51 acting
api_count: 21
apis:
- description: The next-generation iNaturalist API (v2) currently in development, designed to eventually replace v0 and v1 endpoints. Provides access to observation data with improved performance and response format
  name: iNaturalist API v2
  slug: inaturalist-api-v2
- description: Create, delete, and vote
  name: iNaturalist Annotations API
  slug: inaturalist-annotations-api
- description: Create, update, and delete
  name: iNaturalist Comments API
  slug: inaturalist-comments-api
- description: Search and fetch
  name: iNaturalist Controlled Terms API
  slug: inaturalist-controlled-terms-api
- description: Create, update, and delete flags
  name: iNaturalist Flags API
  slug: inaturalist-flags-api
- description: Create, update, and delete
  name: iNaturalist Identifications API
  slug: inaturalist-identifications-api
- description: Create, fetch, delete
  name: iNaturalist Messages API
  slug: inaturalist-messages-api
- description: Create, update, and delete
  name: iNaturalist Observation Field Values API
  slug: inaturalist-observation-field-values-api
- description: Create and delete
  name: iNaturalist Observation Photos API
  slug: inaturalist-observation-photos-api
- description: Map observation search results
  name: iNaturalist Observation Tiles API
  slug: inaturalist-observation-tiles-api
- description: CRUD, search, faving, quality metrics, stats, and more
  name: iNaturalist Observations API
  slug: inaturalist-observations-api
- description: The Photos API from iNaturalist — 1 operation(s) for photos.
  name: iNaturalist Photos API
  slug: inaturalist-photos-api
- description: Search and fetch
  name: iNaturalist Places API
  slug: inaturalist-places-api
- description: Place geometry and taxon range tiles
  name: iNaturalist Polygon Tiles API
  slug: inaturalist-polygon-tiles-api
- description: Fetch site and project posts
  name: iNaturalist Posts API
  slug: inaturalist-posts-api
- description: Create, update, and delete
  name: iNaturalist Project Observations API
  slug: inaturalist-project-observations-api
- description: Search and fetch projects and members
  name: iNaturalist Projects API
  slug: inaturalist-projects-api
- description: Site search
  name: iNaturalist Search API
  slug: inaturalist-search-api
- description: Search and fetch
  name: iNaturalist Taxa API
  slug: inaturalist-taxa-api
- description: Fetch and update
  name: iNaturalist Users API
  slug: inaturalist-users-api
- description: JSON for observation tiles
  name: iNaturalist UTFGrid API
  slug: inaturalist-utfgrid-api
artifact_total: 204
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inaturalist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inaturalist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inaturalist-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.inaturalist.org/pages/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.inaturalist.org/pages/api+reference
- group: operate
  title: ''
  type: Forums
  url: https://forum.inaturalist.org
- group: build
  title: ''
  type: GitHub
  url: https://github.com/inaturalist
- group: company
  title: ''
  type: Blog
  url: https://www.inaturalist.org/blog
- group: operate
  title: ''
  type: Help
  url: https://help.inaturalist.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inaturalist.org/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inaturalist.org/pages/privacy
- group: other
  title: ''
  type: RecommendedPractices
  url: https://www.inaturalist.org/pages/api+recommended+practices
- group: start
  title: ''
  type: Login
  url: https://www.inaturalist.org/login
- group: start
  title: ''
  type: Signup
  url: https://www.inaturalist.org/signup
- group: auth
  title: ''
  type: OAuthApplications
  url: https://www.inaturalist.org/oauth/applications/new
- group: operate
  title: ''
  type: Status
  url: https://status.inaturalist.org
created: '2026-06-13'
description: iNaturalist is a nature observation platform and citizen science network that connects people to nature through biodiversity observation and identification. The iNaturalist API provides programmatic access to over 200 million wildlife observations, species identifications, taxon data, and biodiversity records contributed by citizen scientists worldwide. The API supports reading and writing observations, taxa lookups, identifications, places, projects, and user data across v0, v1, and v2 endpoints.
examples:
- key_count: 6
  name: Delete Annotations Id
  slug: delete-annotations-id
- key_count: 6
  name: Delete Comments Id
  slug: delete-comments-id
- key_count: 6
  name: Delete Flags Id
  slug: delete-flags-id
- key_count: 6
  name: Delete Identifications Id
  slug: delete-identifications-id
- key_count: 6
  name: Delete Messages Id
  slug: delete-messages-id
- key_count: 6
  name: Delete Observation_Field_Values Id
  slug: delete-observation_field_values-id
- key_count: 6
  name: Delete Observation_Photos Id
  slug: delete-observation_photos-id
- key_count: 6
  name: Delete Observations Id Quality Metric
  slug: delete-observations-id-quality-metric
- key_count: 6
  name: Delete Observations Id Review
  slug: delete-observations-id-review
- key_count: 6
  name: Delete Observations Id Unfave
  slug: delete-observations-id-unfave
- key_count: 6
  name: Delete Observations Id
  slug: delete-observations-id
- key_count: 6
  name: Delete Posts Id
  slug: delete-posts-id
- key_count: 6
  name: Delete Project_Observations Id
  slug: delete-project_observations-id
- key_count: 6
  name: Delete Projects Id Leave
  slug: delete-projects-id-leave
- key_count: 6
  name: Delete Projects Id Remove
  slug: delete-projects-id-remove
- key_count: 6
  name: Delete Users Id Mute
  slug: delete-users-id-mute
- key_count: 6
  name: Delete Votes Unvote Annotation Id
  slug: delete-votes-unvote-annotation-id
- key_count: 6
  name: Delete Votes Unvote Observation Id
  slug: delete-votes-unvote-observation-id
- key_count: 6
  name: Get Colored_Heatmap Zoom X Y.Grid.Json
  slug: get-colored_heatmap-zoom-x-y.grid.json
- key_count: 6
  name: Get Colored_Heatmap Zoom X Y.Png
  slug: get-colored_heatmap-zoom-x-y.png
- key_count: 6
  name: Get Controlled_Terms For_Taxon
  slug: get-controlled_terms-for_taxon
- key_count: 6
  name: Get Controlled_Terms
  slug: get-controlled_terms
- key_count: 6
  name: Get Grid Zoom X Y.Grid.Json
  slug: get-grid-zoom-x-y.grid.json
- key_count: 6
  name: Get Grid Zoom X Y.Png
  slug: get-grid-zoom-x-y.png
- key_count: 6
  name: Get Heatmap Zoom X Y.Grid.Json
  slug: get-heatmap-zoom-x-y.grid.json
- key_count: 6
  name: Get Heatmap Zoom X Y.Png
  slug: get-heatmap-zoom-x-y.png
- key_count: 6
  name: Get Identifications Categories
  slug: get-identifications-categories
- key_count: 6
  name: Get Identifications Id
  slug: get-identifications-id
- key_count: 6
  name: Get Identifications Identifiers
  slug: get-identifications-identifiers
- key_count: 6
  name: Get Identifications Observers
  slug: get-identifications-observers
- key_count: 6
  name: Get Identifications Recent_Taxa
  slug: get-identifications-recent_taxa
- key_count: 6
  name: Get Identifications Similar_Species
  slug: get-identifications-similar_species
- key_count: 6
  name: Get Identifications Species_Counts
  slug: get-identifications-species_counts
- key_count: 6
  name: Get Identifications
  slug: get-identifications
- key_count: 6
  name: Get Messages Id
  slug: get-messages-id
- key_count: 6
  name: Get Messages Unread
  slug: get-messages-unread
- key_count: 6
  name: Get Messages
  slug: get-messages
- key_count: 6
  name: Get Observations Deleted
  slug: get-observations-deleted
- key_count: 6
  name: Get Observations Histogram
  slug: get-observations-histogram
- key_count: 6
  name: Get Observations Id Subscriptions
  slug: get-observations-id-subscriptions
- key_count: 6
  name: Get Observations Id Taxon_Summary
  slug: get-observations-id-taxon_summary
- key_count: 6
  name: Get Observations Id
  slug: get-observations-id
- key_count: 6
  name: Get Observations Identifiers
  slug: get-observations-identifiers
- key_count: 6
  name: Get Observations Observers
  slug: get-observations-observers
- key_count: 6
  name: Get Observations Popular_Field_Values
  slug: get-observations-popular_field_values
- key_count: 6
  name: Get Observations Species_Counts
  slug: get-observations-species_counts
- key_count: 6
  name: Get Observations Updates
  slug: get-observations-updates
- key_count: 6
  name: Get Observations
  slug: get-observations
- key_count: 6
  name: Get Places Autocomplete
  slug: get-places-autocomplete
- key_count: 6
  name: Get Places Id
  slug: get-places-id
- key_count: 6
  name: Get Places Nearby
  slug: get-places-nearby
- key_count: 6
  name: Get Places Place_Id Zoom X Y.Png
  slug: get-places-place_id-zoom-x-y.png
- key_count: 6
  name: Get Points Zoom X Y.Grid.Json
  slug: get-points-zoom-x-y.grid.json
- key_count: 6
  name: Get Points Zoom X Y.Png
  slug: get-points-zoom-x-y.png
- key_count: 6
  name: Get Posts For_User
  slug: get-posts-for_user
- key_count: 6
  name: Get Posts
  slug: get-posts
- key_count: 6
  name: Get Projects Autocomplete
  slug: get-projects-autocomplete
- key_count: 6
  name: Get Projects Id Members
  slug: get-projects-id-members
- key_count: 6
  name: Get Projects Id Membership
  slug: get-projects-id-membership
- key_count: 6
  name: Get Projects Id Subscriptions
  slug: get-projects-id-subscriptions
- key_count: 6
  name: Get Projects Id
  slug: get-projects-id
- key_count: 6
  name: Get Projects
  slug: get-projects
- key_count: 6
  name: Get Search
  slug: get-search
- key_count: 6
  name: Get Taxa Autocomplete
  slug: get-taxa-autocomplete
- key_count: 6
  name: Get Taxa Id
  slug: get-taxa-id
- key_count: 6
  name: Get Taxa
  slug: get-taxa
- key_count: 6
  name: Get Taxon_Places Taxon_Id Zoom X Y.Png
  slug: get-taxon_places-taxon_id-zoom-x-y.png
- key_count: 6
  name: Get Taxon_Ranges Taxon_Id Zoom X Y.Png
  slug: get-taxon_ranges-taxon_id-zoom-x-y.png
- key_count: 6
  name: Get Users Autocomplete
  slug: get-users-autocomplete
- key_count: 6
  name: Get Users Id Projects
  slug: get-users-id-projects
- key_count: 6
  name: Get Users Id
  slug: get-users-id
- key_count: 6
  name: Get Users Me
  slug: get-users-me
- key_count: 6
  name: Post Annotations
  slug: post-annotations
- key_count: 6
  name: Post Comments
  slug: post-comments
- key_count: 6
  name: Post Flags
  slug: post-flags
- key_count: 6
  name: Post Identifications
  slug: post-identifications
- key_count: 6
  name: Post Messages
  slug: post-messages
- key_count: 6
  name: Post Observation_Field_Values
  slug: post-observation_field_values
- key_count: 6
  name: Post Observation_Photos
  slug: post-observation_photos
- key_count: 6
  name: Post Observations Id Fave
  slug: post-observations-id-fave
- key_count: 6
  name: Post Observations Id Quality Metric
  slug: post-observations-id-quality-metric
- key_count: 6
  name: Post Observations Id Review
  slug: post-observations-id-review
- key_count: 6
  name: Post Observations
  slug: post-observations
- key_count: 6
  name: Post Photos
  slug: post-photos
- key_count: 6
  name: Post Posts
  slug: post-posts
- key_count: 6
  name: Post Project_Observations
  slug: post-project_observations
- key_count: 6
  name: Post Projects Id Add
  slug: post-projects-id-add
- key_count: 6
  name: Post Projects Id Join
  slug: post-projects-id-join
- key_count: 6
  name: Post Subscriptions Observation Id Subscribe
  slug: post-subscriptions-observation-id-subscribe
- key_count: 6
  name: Post Subscriptions Project Id Subscribe
  slug: post-subscriptions-project-id-subscribe
- key_count: 6
  name: Post Users Id Mute
  slug: post-users-id-mute
- key_count: 6
  name: Post Users Resend_Confirmation
  slug: post-users-resend_confirmation
- key_count: 6
  name: Post Votes Vote Annotation Id
  slug: post-votes-vote-annotation-id
- key_count: 6
  name: Post Votes Vote Observation Id
  slug: post-votes-vote-observation-id
- key_count: 6
  name: Put Comments Id
  slug: put-comments-id
- key_count: 6
  name: Put Flags Id
  slug: put-flags-id
- key_count: 6
  name: Put Identifications Id
  slug: put-identifications-id
- key_count: 6
  name: Put Observation_Field_Values Id
  slug: put-observation_field_values-id
- key_count: 6
  name: Put Observation_Photos Id
  slug: put-observation_photos-id
- key_count: 6
  name: Put Observations Id Viewed_Updates
  slug: put-observations-id-viewed_updates
- key_count: 6
  name: Put Observations Id
  slug: put-observations-id
- key_count: 6
  name: Put Posts Id
  slug: put-posts-id
- key_count: 6
  name: Put Project_Observations Id
  slug: put-project_observations-id
- key_count: 6
  name: Put Users Id
  slug: put-users-id
- key_count: 6
  name: Put Users Update_Session
  slug: put-users-update_session
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://static.inaturalist.org/sites/1-logo.svg
json_schemas:
- name: Annotation
  property_count: 8
  slug: annotation
- name: AutocompleteTaxon
  property_count: 0
  slug: autocompletetaxon
- name: BaseResponse
  property_count: 3
  slug: baseresponse
- name: Color
  property_count: 2
  slug: color
- name: Comment
  property_count: 9
  slug: comment
- name: ConservationStatus
  property_count: 3
  slug: conservationstatus
- name: CorePlace
  property_count: 3
  slug: coreplace
- name: CoreTaxon
  property_count: 8
  slug: coretaxon
- name: DateDetails
  property_count: 6
  slug: datedetails
- name: Error
  property_count: 2
  slug: error
- name: EstablishmentMeans
  property_count: 2
  slug: establishmentmeans
- name: Fave
  property_count: 4
  slug: fave
- name: FieldValue
  property_count: 2
  slug: fieldvalue
- name: Flag
  property_count: 6
  slug: flag
- name: Identification
  property_count: 21
  slug: identification
- name: IdentificationsResponse
  property_count: 0
  slug: identificationsresponse
- name: Message
  property_count: 9
  slug: message
- name: MessagesResponse
  property_count: 0
  slug: messagesresponse
- name: ModeratorAction
  property_count: 6
  slug: moderatoraction
- name: NearbyPlacesResponse
  property_count: 0
  slug: nearbyplacesresponse
- name: NonOwnerIdentification
  property_count: 5
  slug: nonowneridentification
- name: Observation
  property_count: 74
  slug: observation
- name: ObservationPhoto
  property_count: 4
  slug: observationphoto
- name: ObservationsObserversResponse
  property_count: 0
  slug: observationsobserversresponse
- name: ObservationsResponse
  property_count: 0
  slug: observationsresponse
- name: ObservationsShowResponse
  property_count: 0
  slug: observationsshowresponse
- name: ObservationTaxon
  property_count: 0
  slug: observationtaxon
- name: Outlink
  property_count: 3
  slug: outlink
- name: Photo
  property_count: 4
  slug: photo
- name: PlacesResponse
  property_count: 0
  slug: placesresponse
- name: PointGeoJson
  property_count: 2
  slug: pointgeojson
- name: PolygonGeoJson
  property_count: 2
  slug: polygongeojson
- name: PostAnnotation
  property_count: 1
  slug: postannotation
- name: PostComment
  property_count: 1
  slug: postcomment
- name: PostFlag
  property_count: 2
  slug: postflag
- name: PostIdentification
  property_count: 1
  slug: postidentification
- name: PostMessage
  property_count: 1
  slug: postmessage
- name: PostObservation
  property_count: 1
  slug: postobservation
- name: PostObservationFieldValue
  property_count: 1
  slug: postobservationfieldvalue
- name: PostObservationPhoto
  property_count: 1
  slug: postobservationphoto
- name: PostObservationVote
  property_count: 2
  slug: postobservationvote
- name: PostPost
  property_count: 2
  slug: postpost
- name: PostProjectAdd
  property_count: 1
  slug: postprojectadd
- name: PostProjectObservation
  property_count: 2
  slug: postprojectobservation
- name: PostQuality
  property_count: 1
  slug: postquality
- name: PostUser
  property_count: 2
  slug: postuser
- name: PostUserUpdateSession
  property_count: 11
  slug: postuserupdatesession
- name: PostVote
  property_count: 1
  slug: postvote
- name: Project
  property_count: 4
  slug: project
- name: ProjectMember
  property_count: 8
  slug: projectmember
- name: ProjectMembersResponse
  property_count: 0
  slug: projectmembersresponse
- name: ProjectObservation
  property_count: 6
  slug: projectobservation
- name: ProjectsResponse
  property_count: 0
  slug: projectsresponse
- name: PutFlag
  property_count: 1
  slug: putflag
- name: QualityMetric
  property_count: 4
  slug: qualitymetric
- name: RawConservationStatus
  property_count: 6
  slug: rawconservationstatus
- name: ShowObservation
  property_count: 0
  slug: showobservation
- name: ShowPlace
  property_count: 0
  slug: showplace
- name: ShowTaxon
  property_count: 0
  slug: showtaxon
- name: Sound
  property_count: 8
  slug: sound
- name: SpeciesCountsResponse
  property_count: 0
  slug: speciescountsresponse
- name: TaxaAutocompleteResponse
  property_count: 0
  slug: taxaautocompleteresponse
- name: TaxaShowResponse
  property_count: 0
  slug: taxashowresponse
- name: TaxonConservationStatus
  property_count: 0
  slug: taxonconservationstatus
- name: TaxonPhoto
  property_count: 0
  slug: taxonphoto
- name: UpdateProjectObservation
  property_count: 1
  slug: updateprojectobservation
- name: User
  property_count: 15
  slug: user
- name: UserCountsResponse
  property_count: 0
  slug: usercountsresponse
- name: UTFGridResponse
  property_count: 3
  slug: utfgridresponse
- name: Vote
  property_count: 5
  slug: vote
jsonld:
- class_count: 20
  name: Api Context
  property_count: 0
  slug: api
layout: provider
modified: '2026-06-13'
name: iNaturalist
nav: Providers
network: true
overview: 'iNaturalist publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, Comments API, Controlled Terms API, and 17 more. Tagged areas include Biodiversity, Nature, Citizen Science, Wildlife, and Observations.


  The iNaturalist catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  iNaturalist''s developer surface includes authentication, developer portal, documentation, GitHub presence, engineering blog, signup flow, status page, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 27
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: iNaturalist API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: inaturalist-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 52.8
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 51.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inaturalist/refs/heads/main/screenshots/inaturalist-2026-06-20T183309.png
security:
- kind: authentication
  name: Inaturalist Authentication
  slug: inaturalist-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Inaturalist Domain Security
  slug: inaturalist-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inaturalist
tags:
- Biodiversity
- Nature
- Citizen Science
- Wildlife
- Observations
- Taxa
- Ecology
website: https://www.inaturalist.org/pages/developers
---
