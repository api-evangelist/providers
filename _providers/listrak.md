---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Listrak Agentic Access
  operation_count: 131
  slug: listrak-agentic-access
  summary_line: 131 operations · 57 acting
api_count: 15
apis:
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: Endpoints to manage app push devices.
  name: Listrak App Push Mobile Client Device API
  phrasing_intents:
  - id: createAppPushDevice
    intent: Register a device for push notifications
    question: How do I register a new phone so my app can receive Listrak push notifications?
  - id: getAppPushDevice
    intent: Look up a registered push device
    question: Can I see what information is stored for a push device I registered?
  - id: updateAppPushDevice
    intent: Replace a push device's registration
    question: How do I fully replace a device record with a new token and platform?
  - id: patchAppPushDevice
    intent: Partially update a push device
    question: Can I change just one field on a push device, like its app version, without resending everything?
  phrasing_ops: 4
  slug: listrak-app-push-mobile-client-device-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: Endpoints to manage app push mobile client engagements.
  name: Listrak App Push Mobile Client Engagements API
  phrasing_intents:
  - id: createMobileDeviceEngagementEvent
    intent: Record a push engagement from a device
    question: How do I report that a user opened or interacted with a push notification?
  phrasing_ops: 1
  slug: listrak-app-push-mobile-client-engagements-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The BroadcastMessage API from Listrak — 1 operation(s) for broadcastmessage.
  name: Listrak BroadcastMessage API
  phrasing_intents:
  - id: BroadcastMessage_PostImmediateBroadcast
    intent: Send an SMS broadcast immediately
    question: How do I blast a text message right now to everyone subscribed on an SMS list?
  phrasing_ops: 1
  slug: listrak-broadcastmessage-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Campaign API from Listrak — 2 operation(s) for campaign.
  name: Listrak Campaign API
  phrasing_intents:
  - id: Campaign_GetCampaignCollection
    intent: List campaigns on an email list
    question: Which campaigns exist on one of my email lists?
  - id: Campaign_PostCampaignResource
    intent: Create a campaign on a list
    question: How do I add a new campaign to an email list for grouping messages?
  - id: Campaign_GetCampaignResource
    intent: Get one campaign's details
    question: How can I look up a single campaign by its ID on a list?
  - id: Campaign_PutCampaignResource
    intent: Rename an existing campaign
    question: Can I rename a campaign I already created?
  - id: Campaign_DeleteCampaignResource
    intent: Delete a campaign
    question: How do I remove a campaign I no longer need from a list?
  phrasing_ops: 5
  slug: listrak-campaign-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Contact API from Listrak — 8 operation(s) for contact.
  name: Listrak Contact API
  phrasing_intents:
  - id: Contact_GetContactCollection
    intent: List email contacts on a list
    question: How do I pull every email subscriber on one of my lists?
  - id: Contact_PostContactResource
    intent: Create or update an email contact
    question: How do I add or update an email subscriber on a list?
  - id: Contact_GetContactResourceByIdentifier
    intent: Look up an email contact
    question: How do I find a single subscriber on an email list by their address?
  - id: getV1ShortCodeBySenderCodeIdPhoneListByPhoneListIdContact
    intent: List contacts on an SMS list
    question: How do I get all the phone contacts on an SMS list?
  - id: Contact_PostContactListResource
    intent: Create and subscribe an SMS contact
    question: How do I add a new phone number and subscribe it to an SMS list in one step?
  - id: Contact_GetContactResource
    intent: Look up an SMS contact by phone number
    question: How do I check an SMS contact's profile fields and opt-out status by phone number?
  - id: Contact_PutContactResource
    intent: Update an SMS contact's profile
    question: How do I update an existing texting contact's name or postal code?
  - id: Contact_GetOptOuts
    intent: List opt-outs for an SMS sender code
    question: Who has opted out of texts across my whole sender code?
  phrasing_ops: 10
  slug: listrak-contact-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ContactListSubscription API from Listrak — 3 operation(s) for contactlistsubscription.
  name: Listrak ContactListSubscription API
  phrasing_intents:
  - id: ContactListSubscription_GetContactListCollection
    intent: List a phone contact's SMS lists
    question: Which SMS lists is a phone number subscribed to?
  - id: ContactListSubscription_PostContactListSubscription
    intent: Subscribe an existing contact to an SMS list
    question: How do I add a phone number that already exists on my sender code to another SMS list?
  - id: ContactListSubscription_DeleteUnsubscribeContactListSubscription
    intent: Unsubscribe a contact from an SMS list
    question: How do I remove a phone number from one SMS list without opting it out everywhere?
  phrasing_ops: 3
  slug: listrak-contactlistsubscription-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ContactSegmentationField API from Listrak — 1 operation(s) for contactsegmentationfield.
  name: Listrak ContactSegmentationField API
  phrasing_intents:
  - id: ContactSegmentationField_PostContactSegmentationFieldValuesResource
    intent: Bulk update contact profile field values
    question: How do I update profile field values for many contacts on a list at once?
  phrasing_ops: 1
  slug: listrak-contactsegmentationfield-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Content API from Listrak — 2 operation(s) for content.
  name: Listrak Content API
  phrasing_intents:
  - id: Content_GetContentCollection
    intent: List content library blocks
    question: What content blocks are in my content library?
  - id: Content_PostCreateContent
    intent: Create a content block
    question: How do I add a new HTML content block to the content library?
  - id: Content_GetContentResource
    intent: Get a content block
    question: How do I fetch the HTML and text of one content block?
  - id: Content_PutUpdateContent
    intent: Update a content block
    question: Can I edit a content block that's used in live dynamic content?
  phrasing_ops: 4
  slug: listrak-content-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ContentFolder API from Listrak — 1 operation(s) for contentfolder.
  name: Listrak ContentFolder API
  phrasing_intents:
  - id: ContentFolder_GetContentFolderCollection
    intent: List content library folders
    question: What folders are in my content library?
  phrasing_ops: 1
  slug: listrak-contentfolder-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Conversation API from Listrak — 2 operation(s) for conversation.
  name: Listrak Conversation API
  phrasing_intents:
  - id: Conversation_GetConversationCollection
    intent: List conversations on a list
    question: Which conversations (automated email journeys) are set up on a list?
  - id: Conversation_GetConversationResource
    intent: Get a conversation
    question: How do I look up one conversation by its ID?
  phrasing_ops: 2
  slug: listrak-conversation-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ConversationMessage API from Listrak — 2 operation(s) for conversationmessage.
  name: Listrak ConversationMessage API
  phrasing_intents:
  - id: ConversationMessage_GetConversationMessageCollection
    intent: List messages in a conversation
    question: What messages make up a conversation?
  - id: ConversationMessage_GetConversationMessageResource
    intent: Get a conversation message
    question: How do I retrieve one specific message within a conversation?
  phrasing_ops: 2
  slug: listrak-conversationmessage-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ConversationMessageActivity API from Listrak — 1 operation(s) for conversationmessageactivity.
  name: Listrak ConversationMessageActivity API
  phrasing_intents:
  - id: ConversationMessageActivity_GetConversationMessageActivityCollection
    intent: Get activity for a conversation message
    question: Who opened or clicked a particular conversation message?
  phrasing_ops: 1
  slug: listrak-conversationmessageactivity-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ConversationMessageLink API from Listrak — 2 operation(s) for conversationmessagelink.
  name: Listrak ConversationMessageLink API
  phrasing_intents:
  - id: ConversationMessageLink_GetConversationMessageLinkCollection
    intent: List links in a conversation message
    question: What links are tracked in a conversation message?
  - id: ConversationMessageLink_GetConversationMessageLinkResource
    intent: Get one link in a conversation message
    question: How do I look up a single tracked link in a conversation message?
  phrasing_ops: 2
  slug: listrak-conversationmessagelink-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ConversationMessageLinkClicker API from Listrak — 1 operation(s) for conversationmessagelinkclicker.
  name: Listrak ConversationMessageLinkClicker API
  phrasing_intents:
  - id: ConversationMessageLinkClicker_GetMessageLinkClickerCollection
    intent: List who clicked a conversation message link
    question: Which contacts clicked a specific link in a conversation message?
  phrasing_ops: 1
  slug: listrak-conversationmessagelinkclicker-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ConversationMessageSummary API from Listrak — 1 operation(s) for conversationmessagesummary.
  name: Listrak ConversationMessageSummary API
  phrasing_intents:
  - id: ConversationMessageSummary_GetMessageSummaryResource
    intent: Get stats summary for a conversation message
    question: How is a single message in my conversation performing overall?
  phrasing_ops: 1
  slug: listrak-conversationmessagesummary-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ConversationSummary API from Listrak — 1 operation(s) for conversationsummary.
  name: Listrak ConversationSummary API
  phrasing_intents:
  - id: ConversationSummary_GetConversationSummaryResource
    intent: Get stats summary for a conversation
    question: How is a whole conversation performing across all its messages?
  phrasing_ops: 1
  slug: listrak-conversationsummary-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Customer API from Listrak — 1 operation(s) for customer.
  name: Listrak Customer API
  phrasing_intents:
  - id: Customer_PostCustomerCollection
    intent: Import a batch of customers
    question: How do I push my customer records into Listrak in bulk?
  phrasing_ops: 1
  slug: listrak-customer-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Event API from Listrak — 2 operation(s) for event.
  name: Listrak Event API
  phrasing_intents:
  - id: Event_GetEventCollection
    intent: List events on a list
    question: What subscription events are defined on an email list?
  - id: Event_PostEventResource
    intent: Create an event on a list
    question: How do I add a new event to an email list?
  - id: Event_GetEventResource
    intent: Get an event
    question: How do I look up one event by ID on a list?
  - id: Event_PutEventResource
    intent: Update an event
    question: Can I rename an existing event or change its status?
  phrasing_ops: 4
  slug: listrak-event-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The EventGroup API from Listrak — 2 operation(s) for eventgroup.
  name: Listrak EventGroup API
  phrasing_intents:
  - id: EventGroup_GetEventGroupCollection
    intent: List event groups on a list
    question: What event groups exist on my list?
  - id: EventGroup_PostEventGroupResource
    intent: Create an event group
    question: How do I create a group to organize events on a list?
  - id: EventGroup_GetEventGroupResource
    intent: Get an event group
    question: How do I look up one event group by its ID?
  - id: EventGroup_PutEventGroupResource
    intent: Rename an event group
    question: Can I rename an event group that already exists?
  - id: EventGroup_DeleteEventGroupResource
    intent: Delete an event group
    question: How do I remove an event group from a list?
  phrasing_ops: 5
  slug: listrak-eventgroup-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: REST endpoints to manage Custom Events.
  name: Listrak Events API
  phrasing_intents:
  - id: postEvents
    intent: Post custom events
    question: How do I send custom events from my system into Listrak?
  phrasing_ops: 1
  slug: listrak-events-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Folder API from Listrak — 2 operation(s) for folder.
  name: Listrak Folder API
  phrasing_intents:
  - id: Folder_GetFolderCollection
    intent: List account folders
    question: What folders do I have for organizing lists?
  - id: Folder_PostFolderResource
    intent: Create a folder
    question: How do I create a new folder to organize my lists?
  - id: Folder_GetFolderResource
    intent: Get a folder
    question: How do I look up one folder by its ID?
  - id: Folder_PutFolderResource
    intent: Rename a folder
    question: Can I rename a folder that already exists?
  phrasing_ops: 4
  slug: listrak-folder-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Forget API from Listrak — 2 operation(s) for forget.
  name: Listrak Forget API
  phrasing_intents:
  - id: Forget_GetForgetRequest
    intent: Check a forget request's status
    question: Has my data deletion (forget) request finished processing?
  - id: Forget_PostForgetRequest
    intent: Submit a request to forget a person
    question: How do I erase someone's personal data for a privacy request?
  phrasing_ops: 2
  slug: listrak-forget-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The List API from Listrak — 2 operation(s) for list.
  name: Listrak List API
  phrasing_intents:
  - id: List_GetListCollection
    intent: List all email lists
    question: What email lists are in my account?
  - id: List_PostListResource
    intent: Create an email list
    question: How do I create a new email list?
  - id: List_GetListResourceById
    intent: Get an email list's settings
    question: How do I see the settings of one email list?
  - id: List_PutListResource
    intent: Update an email list's settings
    question: Can I change the name or from address of an existing list?
  - id: List_DeleteListResource
    intent: Delete an email list
    question: How do I delete an email list I no longer use?
  phrasing_ops: 5
  slug: listrak-list-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ListImportContact API from Listrak — 1 operation(s) for listimportcontact.
  name: Listrak ListImportContact API
  phrasing_intents:
  - id: ListImportContact_GetListImportContactCollection
    intent: List contacts from a list import
    question: Which contacts came in through a specific list import?
  phrasing_ops: 1
  slug: listrak-listimportcontact-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ListImportStatus API from Listrak — 1 operation(s) for listimportstatus.
  name: Listrak ListImportStatus API
  phrasing_intents:
  - id: ListImportStatus_GetListImportStatusResource
    intent: Check a list import's status
    question: Is my list import still running or has it finished?
  phrasing_ops: 1
  slug: listrak-listimportstatus-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The ListImportSummary API from Listrak — 1 operation(s) for listimportsummary.
  name: Listrak ListImportSummary API
  phrasing_intents:
  - id: ListImportSummary_GetListImportSummaryResource
    intent: Get a list import's result summary
    question: How many records were processed in a finished list import?
  phrasing_ops: 1
  slug: listrak-listimportsummary-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Message API from Listrak — 2 operation(s) for message.
  name: Listrak Message API
  phrasing_intents:
  - id: Message_GetMessageCollection
    intent: List messages sent on a list
    question: What email messages have been sent on a list?
  - id: Message_PostMessageResource
    intent: Send an email message to a list
    question: How do I send a new email blast to a list?
  - id: Message_GetMessageResource
    intent: Get a sent message
    question: How do I retrieve one email message by its ID?
  phrasing_ops: 3
  slug: listrak-message-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The MessageActivity API from Listrak — 1 operation(s) for messageactivity.
  name: Listrak MessageActivity API
  phrasing_intents:
  - id: MessageActivity_GetMessageActivityCollection
    intent: Get activity for an email message
    question: Who opened, clicked or bounced on an email I sent?
  phrasing_ops: 1
  slug: listrak-messageactivity-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The MessageLink API from Listrak — 2 operation(s) for messagelink.
  name: Listrak MessageLink API
  phrasing_intents:
  - id: MessageLink_GetMessageLinkCollection
    intent: List links in an email message
    question: What links are tracked in an email I sent?
  - id: MessageLink_GetMessageLinkResource
    intent: Get one link in an email message
    question: How do I look up a single tracked link in a message?
  phrasing_ops: 2
  slug: listrak-messagelink-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The MessageLinkClicker API from Listrak — 1 operation(s) for messagelinkclicker.
  name: Listrak MessageLinkClicker API
  phrasing_intents:
  - id: MessageLinkClicker_GetMessageLinkClickerCollection
    intent: List who clicked an email link
    question: Which subscribers clicked a specific link in my email?
  phrasing_ops: 1
  slug: listrak-messagelinkclicker-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The MessageStatus API from Listrak — 1 operation(s) for messagestatus.
  name: Listrak MessageStatus API
  phrasing_intents:
  - id: MessageStatus_GetMessageStatusResource
    intent: Check an email message's send status
    question: Has my email finished sending yet?
  phrasing_ops: 1
  slug: listrak-messagestatus-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Messagestream API from Listrak — 1 operation(s) for messagestream.
  name: Listrak Messagestream API
  phrasing_intents:
  - id: getMessageStream
    intent: Read the two-way SMS message stream
    question: How do I pull the recent two-way text conversation for a phone?
  phrasing_ops: 1
  slug: listrak-messagestream-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The MessageSummary API from Listrak — 1 operation(s) for messagesummary.
  name: Listrak MessageSummary API
  phrasing_intents:
  - id: MessageSummary_GetMessageSummaryResource
    intent: Get stats summary for an email message
    question: How did an email I sent perform overall?
  phrasing_ops: 1
  slug: listrak-messagesummary-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Order API from Listrak — 1 operation(s) for order.
  name: Listrak Order API
  phrasing_intents:
  - id: Order_PostOrderCollection
    intent: Import a batch of orders
    question: How do I send my order history into Listrak in bulk?
  phrasing_ops: 1
  slug: listrak-order-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The PhoneList API from Listrak — 2 operation(s) for phonelist.
  name: Listrak PhoneList API
  phrasing_intents:
  - id: PhoneList_GetListCollection
    intent: List SMS lists for a sender code
    question: What SMS lists exist under my sender code?
  - id: PhoneList_GetListResource
    intent: Get an SMS list
    question: How do I look up one SMS list by its ID?
  phrasing_ops: 2
  slug: listrak-phonelist-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Product API from Listrak — 1 operation(s) for product.
  name: Listrak Product API
  phrasing_intents:
  - id: Product_PostProductCollection
    intent: Import a batch of products
    question: How do I load my product catalog into Listrak?
  phrasing_ops: 1
  slug: listrak-product-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The RatingSummary API from Listrak — 1 operation(s) for ratingsummary.
  name: Listrak RatingSummary API
  phrasing_intents:
  - id: RatingSummary_PostRatingSummaryCollection
    intent: Import product rating summaries
    question: How do I send average product ratings into Listrak?
  phrasing_ops: 1
  slug: listrak-ratingsummary-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Review API from Listrak — 1 operation(s) for review.
  name: Listrak Review API
  phrasing_intents:
  - id: Review_PostReviewCollection
    intent: Import product reviews
    question: How do I load customer product reviews into Listrak?
  phrasing_ops: 1
  slug: listrak-review-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The SavedAudience API from Listrak — 1 operation(s) for savedaudience.
  name: Listrak SavedAudience API
  phrasing_intents:
  - id: SavedAudience_GetSavedAudienceResourceCollection
    intent: List saved audiences on a list
    question: What saved audiences do I have on a list?
  phrasing_ops: 1
  slug: listrak-savedaudience-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The SavedMessage API from Listrak — 3 operation(s) for savedmessage.
  name: Listrak SavedMessage API
  phrasing_intents:
  - id: SavedMessage_GetSavedMessageCollection
    intent: List saved messages on a list
    question: What saved (draft) messages exist on a list?
  - id: SavedMessage_PostCreateSavedMessage
    intent: Create a saved message
    question: How do I save an email as a draft to send later?
  - id: SavedMessage_PostSavedMessageSend
    intent: Send a saved message
    question: How do I send an email I previously saved?
  - id: SavedMessage_GetSavedMessageResource
    intent: Get a saved message
    question: How do I view the content of one saved message?
  - id: SavedMessage_PutUpdateSavedMessage
    intent: Update a saved message
    question: Can I edit a saved message's subject or HTML before sending?
  phrasing_ops: 5
  slug: listrak-savedmessage-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Segmentation API from Listrak — 2 operation(s) for segmentation.
  name: Listrak Segmentation API
  phrasing_intents:
  - id: Segmentation_GetPhoneAttribute
    intent: Get an SMS profile field
    question: How do I look up one SMS profile field for my sender code?
  - id: Segmentation_GetPhoneAttributeCollection
    intent: List SMS profile fields
    question: What profile fields are available for SMS contacts on my sender code?
  phrasing_ops: 2
  slug: listrak-segmentation-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The SegmentationField API from Listrak — 2 operation(s) for segmentationfield.
  name: Listrak SegmentationField API
  phrasing_intents:
  - id: SegmentationField_GetSegmentationFieldCollection
    intent: List profile fields in a field group
    question: What profile fields are in a profile field group?
  - id: SegmentationField_PostSegmentationFieldResource
    intent: Create a profile field
    question: How do I add a new custom profile field to a field group?
  - id: SegmentationField_GetSegmentationFieldResource
    intent: Get a profile field
    question: How do I look up one profile field on an email list?
  - id: SegmentationField_PutSegmentationFieldResource
    intent: Update a profile field definition
    question: Can I rename or reposition an existing profile field?
  - id: SegmentationField_DeleteSegmentationFieldResource
    intent: Delete a profile field
    question: How do I remove a profile field definition entirely?
  - id: SegmentationField_DeleteSegmentationFieldValuesResource
    intent: Clear a profile field's values for all contacts
    question: How do I wipe the stored values of a profile field for every subscriber but keep the field?
  phrasing_ops: 6
  slug: listrak-segmentationfield-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The SegmentationFieldGroup API from Listrak — 2 operation(s) for segmentationfieldgroup.
  name: Listrak SegmentationFieldGroup API
  phrasing_intents:
  - id: SegmentationFieldGroup_GetSegmentationFieldGroupCollection
    intent: List profile field groups
    question: What profile field groups exist on my list?
  - id: SegmentationFieldGroup_PostSegmentationFieldGroupResource
    intent: Create a profile field group
    question: How do I create a new group to hold profile fields?
  - id: SegmentationFieldGroup_GetSegmentationFieldGroupResource
    intent: Get a profile field group
    question: How do I look up a single profile field group?
  - id: SegmentationFieldGroup_PutSegmentationFieldGroupResource
    intent: Update a profile field group
    question: Can I rename or reorder an existing profile field group?
  - id: SegmentationFieldGroup_DeleteSegmentationFieldGroupResource
    intent: Delete a profile field group
    question: How do I delete a whole profile field group?
  phrasing_ops: 5
  slug: listrak-segmentationfieldgroup-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Send API from Listrak — 1 operation(s) for send.
  name: Listrak Send API
  phrasing_intents:
  - id: send
    intent: Send a two-way SMS reply on a ticket
    question: How do I send a text reply to a customer from my helpdesk ticket?
  phrasing_ops: 1
  slug: listrak-send-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The SenderCode API from Listrak — 2 operation(s) for sendercode.
  name: Listrak SenderCode API
  phrasing_intents:
  - id: SenderCode_GetShortCodeCollection
    intent: List SMS sender codes
    question: What SMS sender codes does my company have?
  - id: SenderCode_GetShortCodeResource
    intent: Get an SMS sender code
    question: How do I look up the details of one sender code?
  phrasing_ops: 2
  slug: listrak-sendercode-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Tickets API from Listrak — 1 operation(s) for tickets.
  name: Listrak Tickets API
  phrasing_intents:
  - id: openTicket
    intent: Open a two-way SMS support ticket
    question: How do I start a support ticket for an SMS conversation from my helpdesk?
  - id: closeTicket
    intent: Close a two-way SMS support ticket
    question: How do I close the SMS support ticket for a phone once it's resolved?
  phrasing_ops: 2
  slug: listrak-tickets-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The TransactionalMessage API from Listrak — 6 operation(s) for transactionalmessage.
  name: Listrak TransactionalMessage API
  phrasing_intents:
  - id: TransactionalMessage_PostTransactionalMessageSend
    intent: Send a transactional email
    question: How do I send an order confirmation or receipt email to one person?
  - id: TransactionalMessage_GetTransactionalMessageCollection
    intent: List transactional emails on a list
    question: What transactional email templates exist on my email list?
  - id: TransactionalMessage_GetTransactionalMessageResource
    intent: Get a transactional email
    question: How do I look up one transactional email template by ID?
  - id: getV1ShortCodeBySenderCodeIdPhoneListByPhoneListIdTransactionalMessage
    intent: List transactional SMS messages on an SMS list
    question: What transactional text messages are set up on an SMS list?
  - id: getV1ShortCodeBySenderCodeIdPhoneListByPhoneListIdTransactionalMessageByTransactionalMessageId
    intent: Get a transactional SMS message
    question: How do I look up one transactional text message on an SMS list?
  - id: postV1ShortCodeBySenderCodeIdPhoneListByPhoneListIdTransactionalMessageByTransactionalMessageIdMessage
    intent: Send a transactional SMS
    question: How do I text a one-off transactional message, like a shipping alert, to a phone number?
  phrasing_ops: 6
  slug: listrak-transactionalmessage-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The TransactionalMessageActivity API from Listrak — 1 operation(s) for transactionalmessageactivity.
  name: Listrak TransactionalMessageActivity API
  phrasing_intents:
  - id: TransactionalMessageActivity_GetTransactionalMessageActivityCollection
    intent: Get activity for a transactional email
    question: Did a customer open or click a transactional email I sent them?
  phrasing_ops: 1
  slug: listrak-transactionalmessageactivity-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The TransactionalMessageResend API from Listrak — 1 operation(s) for transactionalmessageresend.
  name: Listrak TransactionalMessageResend API
  phrasing_intents:
  - id: TransactionalMessageResend_PostTransactionalMessageResend
    intent: Resend a transactional email
    question: How do I resend a transactional email a customer says they never got?
  phrasing_ops: 1
  slug: listrak-transactionalmessageresend-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Directories API from Listrak — 2 operation(s) for directories.
  name: Listrak Directories API
  phrasing_intents:
  - id: listTopLevelDirectories
    intent: List top-level media directories
    question: What are the root folders in my media library?
  - id: listDirectoryContents
    intent: List a media directory's contents
    question: How do I see the subfolders and files inside a media directory?
  - id: createDirectory
    intent: Create a media subdirectory
    question: How do I make a new folder inside a media directory?
  - id: updateDirectory
    intent: Rename or move a media directory
    question: Can I rename a media folder or move it under another folder?
  - id: deleteDirectory
    intent: Delete a media directory
    question: How do I remove a folder from the media library?
  phrasing_ops: 5
  slug: listrak-directories-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Files API from Listrak — 2 operation(s) for files.
  name: Listrak Files API
  phrasing_intents:
  - id: createFile
    intent: Upload a file to a media directory
    question: How do I upload an image into a media library folder?
  - id: updateFile
    intent: Rename or move a media file
    question: Can I rename an image in the media library or move it to another folder?
  - id: deleteFile
    intent: Delete a media file
    question: How do I remove an image from the media library?
  phrasing_ops: 3
  slug: listrak-files-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The Fonts API from Listrak — 1 operation(s) for fonts.
  name: Listrak Fonts API
  phrasing_intents:
  - id: getFonts
    intent: List available fonts
    question: Which fonts are available to use with my media library?
  phrasing_ops: 1
  slug: listrak-fonts-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: REST endpoints to manage Custom Event Configurations.
  name: Listrak Event Configurations API
  phrasing_intents:
  - id: getEventConfigurations
    intent: List custom event configurations
    question: Which custom event configurations can I post events to?
  - id: getSchemaByEventUid
    intent: Get a custom event configuration's schema
    question: What payload shape does a specific custom event configuration expect?
  phrasing_ops: 2
  slug: listrak-event-configurations-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The IpPool resource exposes all of the IP Pools and their IDs for a user's Account.
  name: Listrak IP Pool API
  phrasing_intents:
  - id: IpPool_GetIpPoolCollection
    intent: List sending IP pools
    question: Which IP pools does my account have for sending email?
  phrasing_ops: 1
  slug: listrak-ip-pool-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The List Import resource is used to supply an import file in order to import data to a list.
  name: Listrak List Import API
  phrasing_intents:
  - id: ListImport_GetListImportCollection
    intent: List imports run on a list
    question: What imports have been run against one of my lists?
  - id: ListImport_PostImportFileResource
    intent: Start a list import from a file
    question: How do I bulk upload a file of subscribers to an email list?
  - id: ListImport_GetListImportResource
    intent: Get a list import
    question: How do I retrieve the details of one list import?
  phrasing_ops: 3
  slug: listrak-list-import-api
- baseURL: https://api.listrak.com
  baseurl_source: declared
  description: The SplitTest resource is used to retrieve information about automated email split tests.
  name: Listrak Split Test API
  phrasing_intents:
  - id: SplitTest_GetSplitTestCollection
    intent: List split tests on a list
    question: What A/B split tests have I run on a list?
  - id: SplitTest_GetSplitTestResource
    intent: Get a split test
    question: How do I look up one A/B split test?
  - id: SplitTest_GetSplitTestMessageResources
    intent: List the variant messages in a split test
    question: Which message variants were sent in a split test?
  phrasing_ops: 3
  slug: listrak-split-test-api
artifact_total: 137
asyncapis:
- description: ''
  name: Listrak Webhooks
  slug: listrak-webhooks
collections:
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device API
  slug: open-listrak-app-push-mobile-client-device-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device app-push-mobile-client-engagements API
  slug: open-listrak-app-push-mobile-client-engagements-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device BroadcastMessage API
  slug: open-listrak-broadcastmessage-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Campaign API
  slug: open-listrak-campaign-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Contact API
  slug: open-listrak-contact-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ContactListSubscription API
  slug: open-listrak-contactlistsubscription-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ContactSegmentationField API
  slug: open-listrak-contactsegmentationfield-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Content API
  slug: open-listrak-content-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ContentFolder API
  slug: open-listrak-contentfolder-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Conversation API
  slug: open-listrak-conversation-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ConversationMessage API
  slug: open-listrak-conversationmessage-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ConversationMessageActivity API
  slug: open-listrak-conversationmessageactivity-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ConversationMessageLink API
  slug: open-listrak-conversationmessagelink-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ConversationMessageLinkClicker API
  slug: open-listrak-conversationmessagelinkclicker-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ConversationMessageSummary API
  slug: open-listrak-conversationmessagesummary-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ConversationSummary API
  slug: open-listrak-conversationsummary-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Customer API
  slug: open-listrak-customer-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Event API
  slug: open-listrak-event-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device EventConfigurations API
  slug: open-listrak-eventconfigurations-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device EventGroup API
  slug: open-listrak-eventgroup-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Events API
  slug: open-listrak-events-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Folder API
  slug: open-listrak-folder-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Forget API
  slug: open-listrak-forget-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device IpPool API
  slug: open-listrak-ippool-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device List API
  slug: open-listrak-list-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ListImport API
  slug: open-listrak-listimport-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ListImportContact API
  slug: open-listrak-listimportcontact-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ListImportStatus API
  slug: open-listrak-listimportstatus-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device ListImportSummary API
  slug: open-listrak-listimportsummary-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Message API
  slug: open-listrak-message-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device MessageActivity API
  slug: open-listrak-messageactivity-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device MessageLink API
  slug: open-listrak-messagelink-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device MessageLinkClicker API
  slug: open-listrak-messagelinkclicker-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device MessageStatus API
  slug: open-listrak-messagestatus-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Messagestream API
  slug: open-listrak-messagestream-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device MessageSummary API
  slug: open-listrak-messagesummary-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Order API
  slug: open-listrak-order-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device PhoneList API
  slug: open-listrak-phonelist-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Product API
  slug: open-listrak-product-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device RatingSummary API
  slug: open-listrak-ratingsummary-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device SavedAudience API
  slug: open-listrak-savedaudience-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device SavedMessage API
  slug: open-listrak-savedmessage-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Segmentation API
  slug: open-listrak-segmentation-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device SegmentationField API
  slug: open-listrak-segmentationfield-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device SegmentationFieldGroup API
  slug: open-listrak-segmentationfieldgroup-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Send API
  slug: open-listrak-send-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device SenderCode API
  slug: open-listrak-sendercode-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device SplitTest API
  slug: open-listrak-splittest-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device Tickets API
  slug: open-listrak-tickets-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device TransactionalMessage API
  slug: open-listrak-transactionalmessage-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device TransactionalMessageActivity API
  slug: open-listrak-transactionalmessageactivity-api
- collection_type: open
  name: Listrak Cross Channel REST app-push-mobile-client-device TransactionalMessageResend API
  slug: open-listrak-transactionalmessageresend-api
common:
- group: other
  href: https://artifacts.apis.io/listrak/capabilities/listrak-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/listrak-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/listrak/agentic-access/listrak-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/listrak-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/listrak/security/listrak-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/listrak-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/listrak/authentication/listrak-authentication.yml
  title: ''
  type: Authentication
  url: authentication/listrak-authentication.yml
- group: auth
  href: https://artifacts.apis.io/listrak/scopes/listrak-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/listrak-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.listrak.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.listrak.com/learn/developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/listrak
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listrak/
- group: company
  title: ''
  type: Blog
  url: https://www.listrak.com/learn/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.listrak.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.listrak.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/Listrak
- group: commercial
  href: https://artifacts.apis.io/listrak/plans/listrak-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/listrak-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/listrak/rate-limits/listrak-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/listrak-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/listrak/finops/listrak-finops.yml
  title: ''
  type: FinOps
  url: finops/listrak-finops.yml
- group: design
  href: https://artifacts.apis.io/listrak/vocabulary/listrak-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/listrak-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/listrak/json-ld/listrak-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/listrak-context.jsonld
- group: build
  href: https://artifacts.apis.io/listrak/packages/listrak-packages.yml
  title: ''
  type: Packages
  url: packages/listrak-packages.yml
- group: build
  href: https://artifacts.apis.io/listrak/packages/listrak-packages.yml
  title: ''
  type: SDKs
  url: packages/listrak-packages.yml
- group: design
  href: https://artifacts.apis.io/listrak/conventions/listrak-conventions.yml
  title: ''
  type: Conventions
  url: conventions/listrak-conventions.yml
- group: design
  href: https://artifacts.apis.io/listrak/errors/listrak-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/listrak-error-codes.yml
- group: design
  href: https://artifacts.apis.io/listrak/lifecycle/listrak-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/listrak-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/listrak/changelog/listrak-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/listrak-changelog.yml
- group: design
  href: https://artifacts.apis.io/listrak/data-model/listrak-data-model.yml
  title: ''
  type: DataModel
  url: data-model/listrak-data-model.yml
- group: design
  href: https://artifacts.apis.io/listrak/conformance/listrak-conformance.yml
  title: ''
  type: Conformance
  url: conformance/listrak-conformance.yml
- group: design
  href: https://artifacts.apis.io/listrak/asyncapi/listrak-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/listrak-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/listrak/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/listrak/llms/listrak-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/listrak-llms.txt
- group: other
  href: https://artifacts.apis.io/listrak/overlays/listrak-security-and-semantics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/listrak-security-and-semantics-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/listrak/security/listrak-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/listrak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.listrak.com/privacy-and-terms/responsible-disclosure
- group: auth
  href: https://artifacts.apis.io/listrak/security/listrak-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/listrak-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.listrak.com/privacy-and-terms/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.listrak.com/learn/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.listrak.com/email
- group: start
  title: ''
  type: GettingStarted
  url: https://help.listrak.com/en/articles/9406951-rest-api-integrations-at-listrak
- group: operate
  title: ''
  type: Support
  url: https://help.listrak.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://www.listrak.com/get-started
- group: start
  title: ''
  type: Login
  url: https://admin.listrak.com/Account/Login.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.listrak.com/privacy-and-terms/acceptable-use-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.listrak.com/privacy-and-terms/privacy-policy
created: 2026-06-13
description: 'Listrak is a retail customer-engagement platform whose public API surface is eight separate REST APIs served from api.listrak.com: Email (83 operations), SMS (20), Data Import (5), Media (9), Mobile App Push (5), Two-Way SMS (4), Cross Channel custom events (3) and Privacy (2). Together they cover contacts and lists, message authoring and transactional sends, profile-field segmentation, behavioral events that drive Journey Hub automations, bulk upsert of retail customers, orders, products and reviews, media library management, mobile device registration, two-way SMS support conversations, and GDPR/CCPA forget requests. Every server-side API authenticates with OAuth 2.0 client_credentials against a single token endpoint at auth.listrak.com, returns a consistent {status, error, message} envelope drawn from a published 68-code error registry, and pages with cursor plus count.'
examples:
- key_count: 4
  name: Listrak Crosschannel_Event Example
  slug: listrak-crosschannel_event-example
- key_count: 4
  name: Listrak Data_Order Example
  slug: listrak-data_order-example
- key_count: 4
  name: Listrak Email_Contact Example
  slug: listrak-email_contact-example
- key_count: 4
  name: Listrak Sms_Subscriber Example
  slug: listrak-sms_subscriber-example
finops:
- has_sources: true
  method: derived
  name: Listrak Finops
  primary_unit: ''
  service_category: ''
  slug: listrak-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listrak.png
json_schemas:
- name: Listrak Crosschannel API Schemas
  property_count: 0
  slug: listrak-crosschannel-schemas
- name: Listrak Data API Schemas
  property_count: 0
  slug: listrak-data-schemas
- name: Listrak Email API Schemas
  property_count: 0
  slug: listrak-email-schemas
- name: Listrak Mobileclient API Schemas
  property_count: 0
  slug: listrak-mobileclient-schemas
- name: Listrak Privacy API Schemas
  property_count: 0
  slug: listrak-privacy-schemas
- name: Listrak Sms API Schemas
  property_count: 0
  slug: listrak-sms-schemas
- name: Listrak Twowaysms API Schemas
  property_count: 0
  slug: listrak-twowaysms-schemas
jsonld:
- class_count: 8
  name: Listrak Context
  property_count: 32
  slug: listrak-context
layout: provider
modified: 2026-08-13
name: Listrak
nav: Providers
network: true
overview: 'Listrak publishes 56 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Push Mobile Client Device API, App Push Mobile Client Engagements API, BroadcastMessage API, and 53 more. Tagged areas include Email Marketing, SMS Marketing, Marketing Automation, Cross-Channel, and Retail.


  The Listrak catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Listrak''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 35 more developer resources.'
plans:
- name: Listrak Plans Pricing
  plan_count: 1
  slug: listrak-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 9
  name: Listrak Rate Limits
  slug: listrak-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Listrak — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: listrak-jsonschema-spectral-rules
scopes:
- name: Listrak Scopes
  scope_count: 10
  slug: listrak-scopes
  summary_line: 10 scopes · clientCredentials
score:
  band: exemplar
  composite: 73.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 78.8
    catalog_earned_first_party: 20.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 81.6
    contract_governance: 28.0
    contract_quality: 71.2
    developer_ergonomics: 60.1
    discoverability: 71.4
    operational_transparency: 84.2
  previous_composite: 72.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 80.4
      total: 56
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/listrak/listrak-2026-06-20T184559.png
security:
- kind: authentication
  name: Listrak Authentication
  slug: listrak-authentication
  summary_line: oauth2/apiKey/http · 4 schemes
- kind: domain-security
  name: Listrak Domain Security
  slug: listrak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Listrak Vulnerability Disclosure
  slug: listrak-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Listrak Trust Center
  slug: listrak-trust-center
  summary_line: trust center published
skill_count: 6
skills:
- name: Honor a GDPR/CCPA forget request in Listrak
  slug: listrak-honor-a-privacy-forget-request
- name: Manage Listrak SMS subscriptions
  slug: listrak-manage-sms-subscriptions
- name: Post Listrak cross-channel custom events
  slug: listrak-post-cross-channel-events
- name: Send a Listrak transactional email
  slug: listrak-send-a-transactional-email
- name: Subscribe and profile a Listrak email contact
  slug: listrak-subscribe-and-profile-a-contact
- name: Sync retail data into Listrak
  slug: listrak-sync-retail-data
slug: listrak
tags:
- Email Marketing
- SMS Marketing
- Marketing Automation
- Cross-Channel
- Retail
- Push Notifications
- Data Import
- Privacy
- E-Commerce
- Customer Data
- Transactional Messaging
- Segmentation
- Product Reviews
- Media Management
- Two-Way SMS
- RCS
website: https://www.listrak.com/
---
