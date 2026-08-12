---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Bigoven Agentic Access
  operation_count: 66
  slug: bigoven-agentic-access
  summary_line: 66 operations · 33 acting
api_count: 7
apis:
- description: The Collection API from BigOven — 3 operation(s) for collection.
  name: BigOven Collection API
  slug: bigoven-collection-api
- description: The GroceryList API from BigOven — 8 operation(s) for grocerylist.
  name: BigOven GroceryList API
  slug: bigoven-grocerylist-api
- description: The Images API from BigOven — 6 operation(s) for images.
  name: BigOven Images API
  slug: bigoven-images-api
- description: The Me API from BigOven — 6 operation(s) for me.
  name: BigOven Me API
  slug: bigoven-me-api
- description: The Note API from BigOven — 3 operation(s) for note.
  name: BigOven Note API
  slug: bigoven-note-api
- description: The Recipe API from BigOven — 21 operation(s) for recipe.
  name: BigOven Recipe API
  slug: bigoven-recipe-api
- description: The Review API from BigOven — 6 operation(s) for review.
  name: BigOven Review API
  slug: bigoven-review-api
artifact_total: 137
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigoven-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigoven-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigoven-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigoven.com
- group: docs
  title: ''
  type: Documentation
  url: https://api2.bigoven.com/web/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bigoven
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigoven-com
- group: company
  title: ''
  type: Blog
  url: https://www.bigoven.com/article
- group: commercial
  title: ''
  type: Pricing
  url: https://api2.bigoven.com/web/documentation/feestructure
- group: other
  title: ''
  type: X
  url: https://x.com/bigoven
- group: commercial
  title: ''
  type: Plans
  url: plans/bigoven-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bigoven-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bigoven-finops.yml
created: '2026-06-13'
description: BigOven is a recipe and meal planning platform providing access to over 1,000,000 recipes via a REST API. Developers can search recipes, retrieve nutritional information, manage cloud-based grocery lists, and build diet and meal planning features. The API is offered by Aisle Ahead, Inc. and supports commercial food, nutrition, diet, and grocery applications.
examples:
- key_count: 7
  name: Collection_Collections
  slug: Collection_Collections
- key_count: 7
  name: Collection_Getcollection
  slug: Collection_GetCollection
- key_count: 7
  name: Collection_Getcollectionmeta
  slug: Collection_GetCollectionMeta
- key_count: 8
  name: Grocerylist_Addrecipe
  slug: GroceryList_AddRecipe
- key_count: 7
  name: Grocerylist_Delete
  slug: GroceryList_Delete
- key_count: 7
  name: Grocerylist_Deleteitembyguid
  slug: GroceryList_DeleteItemByGuid
- key_count: 8
  name: Grocerylist_Department
  slug: GroceryList_Department
- key_count: 7
  name: Grocerylist_Get
  slug: GroceryList_Get
- key_count: 8
  name: Grocerylist_Grocerylistitemguid
  slug: GroceryList_GroceryListItemGuid
- key_count: 7
  name: Grocerylist_Grocerylistremovemarkeditems
  slug: GroceryList_GroceryListRemoveMarkedItems
- key_count: 8
  name: Grocerylist_Post
  slug: GroceryList_Post
- key_count: 8
  name: Grocerylist_Postgrocerylistsync
  slug: GroceryList_PostGroceryListSync
- key_count: 7
  name: Images_Get
  slug: Images_Get
- key_count: 7
  name: Images_Getpendingbyuser
  slug: Images_GetPendingByUser
- key_count: 7
  name: Images_Getrecipephotos
  slug: Images_GetRecipePhotos
- key_count: 7
  name: Images_Getscanimages
  slug: Images_GetScanImages
- key_count: 7
  name: Images_Uploadrecipeimage
  slug: Images_UploadRecipeImage
- key_count: 7
  name: Images_Uploaduseravatar
  slug: Images_UploadUserAvatar
- key_count: 7
  name: Me_Getoptions
  slug: Me_GetOptions
- key_count: 7
  name: Me_Index
  slug: Me_Index
- key_count: 8
  name: Me_Putme
  slug: Me_PutMe
- key_count: 8
  name: Me_Putmepersonal
  slug: Me_PutMePersonal
- key_count: 8
  name: Me_Putmepreferences
  slug: Me_PutMePreferences
- key_count: 7
  name: Me_Skinny
  slug: Me_Skinny
- key_count: 7
  name: Note_Delete
  slug: Note_Delete
- key_count: 7
  name: Note_Get
  slug: Note_Get
- key_count: 7
  name: Note_Getnotes
  slug: Note_GetNotes
- key_count: 8
  name: Note_Post
  slug: Note_Post
- key_count: 8
  name: Note_Put
  slug: Note_Put
- key_count: 7
  name: Recipe_Autocomplete
  slug: Recipe_AutoComplete
- key_count: 7
  name: Recipe_Autocompleteallrecipes
  slug: Recipe_AutoCompleteAllRecipes
- key_count: 7
  name: Recipe_Autocompletemyrecipes
  slug: Recipe_AutoCompleteMyRecipes
- key_count: 7
  name: Recipe_Categories
  slug: Recipe_Categories
- key_count: 7
  name: Recipe_Delete
  slug: Recipe_Delete
- key_count: 8
  name: Recipe_Feedback
  slug: Recipe_Feedback
- key_count: 7
  name: Recipe_Get
  slug: Recipe_Get
- key_count: 7
  name: Recipe_Getactiverecipe
  slug: Recipe_GetActiveRecipe
- key_count: 7
  name: Recipe_Getrandomrecipe
  slug: Recipe_GetRandomRecipe
- key_count: 7
  name: Recipe_Getrecipewithsteps
  slug: Recipe_GetRecipeWithSteps
- key_count: 7
  name: Recipe_Getstep
  slug: Recipe_GetStep
- key_count: 7
  name: Recipe_Getstepnumber
  slug: Recipe_GetStepNumber
- key_count: 7
  name: Recipe_Getsteps
  slug: Recipe_GetSteps
- key_count: 7
  name: Recipe_Getv2
  slug: Recipe_GetV2
- key_count: 7
  name: Recipe_Post
  slug: Recipe_Post
- key_count: 7
  name: Recipe_Put
  slug: Recipe_Put
- key_count: 7
  name: Recipe_Raves
  slug: Recipe_Raves
- key_count: 7
  name: Recipe_Recentviews
  slug: Recipe_RecentViews
- key_count: 7
  name: Recipe_Recipesearch
  slug: Recipe_RecipeSearch
- key_count: 7
  name: Recipe_Recipesearchrandom
  slug: Recipe_RecipeSearchRandom
- key_count: 7
  name: Recipe_Related
  slug: Recipe_Related
- key_count: 6
  name: Recipe_Scan
  slug: Recipe_Scan
- key_count: 7
  name: Recipe_Zaprecipe
  slug: Recipe_ZapRecipe
- key_count: 7
  name: Review_Delete
  slug: Review_Delete
- key_count: 7
  name: Review_Deletereply
  slug: Review_DeleteReply
- key_count: 7
  name: Review_Get
  slug: Review_Get
- key_count: 7
  name: Review_Getreplies
  slug: Review_GetReplies
- key_count: 7
  name: Review_Getreviews
  slug: Review_GetReviews
- key_count: 7
  name: Review_Post
  slug: Review_Post
- key_count: 7
  name: Review_Postreply
  slug: Review_PostReply
- key_count: 7
  name: Review_Put
  slug: Review_Put
- key_count: 8
  name: Review_Putlegacy
  slug: Review_PutLegacy
- key_count: 7
  name: Review_Putreply
  slug: Review_PutReply
- key_count: 7
  name: Get  Recipe Recipeid Review
  slug: get--recipe-recipeId-review
- key_count: 7
  name: Get  Recipe Review Reviewid
  slug: get--recipe-review-reviewId
- key_count: 8
  name: Post  Grocerylist Item
  slug: post--grocerylist-item
- key_count: 8
  name: Put  Me Profile
  slug: put--me-profile
finops:
- name: Bigoven Finops
  service_category: ''
  slug: bigoven-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigoven.png
json_schemas:
- name: API2.Controllers.WebAPI.GroceryListController.DepartmentModel
  property_count: 1
  slug: api2.controllers.webapi.grocerylistcontroller.departmentmodel
- name: API2.Controllers.WebAPI.GroceryListController.PostGroceryListAddLineRequest
  property_count: 1
  slug: api2.controllers.webapi.grocerylistcontroller.postgrocerylistaddlinerequest
- name: API2.Controllers.WebAPI.GroceryListController.PostGroceryListRecipeRequest
  property_count: 3
  slug: api2.controllers.webapi.grocerylistcontroller.postgrocerylistreciperequest
- name: API2.Controllers.WebAPI.GroceryListController.PostGroceryListSyncRequest
  property_count: 2
  slug: api2.controllers.webapi.grocerylistcontroller.postgrocerylistsyncrequest
- name: API2.Controllers.WebAPI.GroceryListController.PostToGroceryListRecipeRequest
  property_count: 5
  slug: api2.controllers.webapi.grocerylistcontroller.posttogrocerylistreciperequest
- name: API2.Controllers.WebAPI.GroceryListController.UpdateItemByGuidRequest
  property_count: 7
  slug: api2.controllers.webapi.grocerylistcontroller.updateitembyguidrequest
- name: API2.Controllers.WebAPI.ImagesController.RecipePhotosResponse
  property_count: 2
  slug: api2.controllers.webapi.imagescontroller.recipephotosresponse
- name: API2.Controllers.WebAPI.MeController.EatingStyle
  property_count: 1
  slug: api2.controllers.webapi.mecontroller.eatingstyle
- name: API2.Controllers.WebAPI.MeController.Option
  property_count: 2
  slug: api2.controllers.webapi.mecontroller.option
- name: API2.Controllers.WebAPI.MeController.PreferenceOptions
  property_count: 1
  slug: api2.controllers.webapi.mecontroller.preferenceoptions
- name: API2.Controllers.WebAPI.NoteController.NoteRequest
  property_count: 10
  slug: api2.controllers.webapi.notecontroller.noterequest
- name: API2.Controllers.WebAPI.ReviewController.PostReplyReq
  property_count: 1
  slug: api2.controllers.webapi.reviewcontroller.postreplyreq
- name: API2.Controllers.WebAPI.ReviewController.ReviewRequest
  property_count: 5
  slug: api2.controllers.webapi.reviewcontroller.reviewrequest
- name: API2.Controllers.WebAPI.ReviewController.ReviewRequestLegacy
  property_count: 7
  slug: api2.controllers.webapi.reviewcontroller.reviewrequestlegacy
- name: API2.GroceryListDepartmentResult
  property_count: 2
  slug: api2.grocerylistdepartmentresult
- name: API2.Models.Accounting
  property_count: 4
  slug: api2.models.accounting
- name: API2.Models.BigOvenUser
  property_count: 6
  slug: api2.models.bigovenuser
- name: API2.Models.Counts
  property_count: 6
  slug: api2.models.counts
- name: API2.Models.Location
  property_count: 3
  slug: api2.models.location
- name: API2.Models.Personal
  property_count: 2
  slug: api2.models.personal
- name: API2.Models.Preference
  property_count: 1
  slug: api2.models.preference
- name: API2.Models.Profile
  property_count: 10
  slug: api2.models.profile
- name: API2.Models.Recipes.FeedbackDTO
  property_count: 1
  slug: api2.models.recipes.feedbackdto
- name: API2.Models.Recipes.RecipeResponse
  property_count: 47
  slug: api2.models.recipes.reciperesponse
- name: API2.Models.Recipes.RecipeVideoResponse
  property_count: 4
  slug: api2.models.recipes.recipevideoresponse
- name: API2.Result
  property_count: 3
  slug: api2.result
- name: BigOven.Model.API.Grocery.GroceryList
  property_count: 4
  slug: bigoven.model.api.grocery.grocerylist
- name: BigOven.Model.API.Grocery.Item
  property_count: 13
  slug: bigoven.model.api.grocery.item
- name: BigOven.Model.API.Image
  property_count: 14
  slug: bigoven.model.api.image
- name: BigOven.Model.API.Ingredient
  property_count: 14
  slug: bigoven.model.api.ingredient
- name: BigOven.Model.API.IngredientInfo
  property_count: 4
  slug: bigoven.model.api.ingredientinfo
- name: BigOven.Model.API.NutritionInfo
  property_count: 23
  slug: bigoven.model.api.nutritioninfo
- name: BigOven.Model.API.Recipe
  property_count: 45
  slug: bigoven.model.api.recipe
- name: BigOven.Model.API.RecipeInfo
  property_count: 24
  slug: bigoven.model.api.recipeinfo
- name: BigOven.Model.API.RecipeNote
  property_count: 10
  slug: bigoven.model.api.recipenote
- name: BigOven.Model.API.RecipeNoteList
  property_count: 2
  slug: bigoven.model.api.recipenotelist
- name: BigOven.Model.API.Reply
  property_count: 6
  slug: bigoven.model.api.reply
- name: BigOven.Model.API.Review
  property_count: 14
  slug: bigoven.model.api.review
- name: BigOven.Model.API.UserInfo
  property_count: 13
  slug: bigoven.model.api.userinfo
- name: BigOven.Model.API.UserInfoTiny
  property_count: 5
  slug: bigoven.model.api.userinfotiny
- name: BigOven.Model.API2.CollectionInfo
  property_count: 11
  slug: bigoven.model.api2.collectioninfo
- name: BigOven.Model.API2.GroceryList
  property_count: 4
  slug: bigoven.model.api2.grocerylist
- name: BigOven.Model.API2.Photo
  property_count: 7
  slug: bigoven.model.api2.photo
- name: BigOven.Model.API2.Recipe
  property_count: 46
  slug: bigoven.model.api2.recipe
- name: BigOven.Model.API2.RecipeInfox
  property_count: 18
  slug: bigoven.model.api2.recipeinfox
- name: BigOven.Model.API2.RecipeNote
  property_count: 10
  slug: bigoven.model.api2.recipenote
- name: BigOven.Model.API2.RecipeSearchResult
  property_count: 3
  slug: bigoven.model.api2.recipesearchresult
- name: BigOven.Model.API2.UserInfoTinyx
  property_count: 5
  slug: bigoven.model.api2.userinfotinyx
- name: BigOven.Model.InstructionStep
  property_count: 3
  slug: bigoven.model.instructionstep
- name: BigOven.Model.RecipeCategory
  property_count: 7
  slug: bigoven.model.recipecategory
- name: BigOven.Model.RecipeInfoDateTuple2
  property_count: 2
  slug: bigoven.model.recipeinfodatetuple2
- name: BigOven.Model.RecipeInfoReviewTuple2
  property_count: 2
  slug: bigoven.model.recipeinforeviewtuple2
- name: BigOven.Model.RecipeInfoTiny
  property_count: 5
  slug: bigoven.model.recipeinfotiny
- name: BigOven.Model.ShoppingListLine
  property_count: 19
  slug: bigoven.model.shoppinglistline
- name: BigOven.Result
  property_count: 3
  slug: bigoven.result
- name: System.Object
  property_count: 0
  slug: system.object
jsonld:
- class_count: 0
  name: Bigoven Context
  property_count: 0
  slug: bigoven
layout: provider
modified: '2026-06-13'
name: BigOven
nav: Providers
network: true
overview: 'BigOven publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Collection API, GroceryList API, Images API, and 4 more. Tagged areas include Recipes, Meal Planning, Grocery Lists, Nutrition, and Food.


  The BigOven catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BigOven''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Bigoven Plans Pricing
  plan_count: 5
  slug: bigoven-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 0
  name: Bigoven Rate Limits
  slug: bigoven-rate-limits
rules:
- name: BigOven API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bigoven-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: -0.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigoven/refs/heads/main/screenshots/bigoven-2026-06-20T173235.png
security:
- kind: authentication
  name: Bigoven Authentication
  slug: bigoven-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Bigoven Domain Security
  slug: bigoven-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bigoven
tags:
- Recipes
- Meal Planning
- Grocery Lists
- Nutrition
- Food
- Cooking
website: https://www.bigoven.com
---
