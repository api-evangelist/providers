---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 270
  human_in_the_loop: 4
  name: Elevenlabs Agentic Access
  operation_count: 452
  slug: elevenlabs-agentic-access
  summary_line: 452 operations · 270 acting · 4 human-in-the-loop
api_count: 12
apis:
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating, managing, and configuring conversational AI agents with voice capabilities.
  name: elevenlabs Agents API
  phrasing_intents:
  - id: listAgents
    intent: List my conversational AI agents
    question: Which voice agents have I built on my ElevenLabs account?
  - id: createAgent
    intent: Create a conversational AI agent
    question: How do I create a voice agent with its own voice, model and tools?
  - id: getAgent
    intent: Get an agent's configuration
    question: What voice, prompt and tools is one of my agents configured with?
  - id: updateAgent
    intent: Update an agent's configuration
    question: Can I change an agent's prompt or voice without resending the whole config?
  - id: deleteAgent
    intent: Delete a conversational agent
    question: How do I permanently delete a voice agent?
  - id: simulateConversation
    intent: Simulate a conversation to test an agent
    question: Can I test my agent against a simulated caller before going live?
  phrasing_ops: 6
  slug: elevenlabs-agents-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for isolating vocals from background noise in audio recordings.
  name: elevenlabs Audio Isolation API
  phrasing_intents:
  - id: audio_isolation
    intent: Remove background noise from audio
    question: Can I clean up a noisy recording so only the voice remains?
  - id: get_audio_isolation_history
    intent: List my past audio isolation jobs
    question: Which files have I run through voice isolation before?
  - id: delete_audio_isolation_history_item
    intent: Delete an audio isolation history item
    question: How do I delete a past noise-removal job and its files?
  - id: audio_isolation_stream
    intent: Remove background noise and stream the result
    question: Can I stream the denoised audio back while a large file is processed?
  phrasing_ops: 4
  slug: elevenlabs-audio-isolation-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating and managing Audio Native embedded players for web content.
  name: elevenlabs Audio Native API
  phrasing_intents:
  - id: create_audio_native_project
    intent: Create an Audio Native embedded player
    question: How do I add a listen-to-this-article audio player to my blog?
  - id: get_audio_native_project_settings_endpoint
    intent: Get an Audio Native player's settings
    question: How do I check the player settings of an Audio Native project?
  - id: audio_native_project_update_content_endpoint
    intent: Upload new article content to an Audio Native project
    question: Can I replace an Audio Native project's article by uploading an HTML or text file?
  - id: audio_native_update_content_from_url
    intent: Refresh Audio Native content from a page URL
    question: I updated my article; how do I get its Audio Native player to pick up the changes?
  phrasing_ops: 4
  slug: elevenlabs-audio-native-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for retrieving and managing conversation sessions and their associated data.
  name: elevenlabs Conversations API
  phrasing_intents:
  - id: listConversations
    intent: List agent conversations
    question: What conversations have my voice agents had recently?
  - id: getConversation
    intent: Get a conversation's transcript and analysis
    question: Can I read the full transcript of a call my agent handled?
  - id: deleteConversation
    intent: Delete a conversation
    question: How do I delete a stored agent conversation and its data?
  - id: getConversationAudio
    intent: Download a conversation's audio recording
    question: Can I listen to the recording of a call my agent took?
  phrasing_ops: 4
  slug: elevenlabs-conversations-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating, managing, and retrieving dubbed audio and video content across languages.
  name: elevenlabs Dubbing API
  phrasing_intents:
  - id: createDubbing
    intent: Dub a video or audio file into another language
    question: How do I dub a video into Spanish with ElevenLabs?
  - id: list_dubs
    intent: List my dubs
    question: Which of my dubs are still in progress and which have finished?
  - id: getDubbing
    intent: Check the status of a dub
    question: Is my dub finished processing yet?
  - id: deleteDubbing
    intent: Delete a dub
    question: How do I permanently delete a dub and its files?
  - id: dubbing_project_create
    intent: Create a dubbing project from a file or URL
    question: How do I set up a dubbing project I can add languages to later?
  - id: dubbing_project_list
    intent: List dubbing projects in my workspace
    question: What dubbing projects exist in my workspace?
  - id: dubbing_project_get
    intent: Get a dubbing project's details
    question: Which language targets are under my dubbing project?
  - id: dubbing_project_delete
    intent: Delete a dubbing project and all its languages
    question: Am I still billed if I delete a dubbing project while a dub is running?
  phrasing_ops: 37
  slug: elevenlabs-dubbing-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing individual dubbing resources including segments, translations, and dubbed output files.
  name: elevenlabs Dubbing Resources API
  phrasing_intents:
  - id: getDubbedAudio
    intent: Download dubbed audio for a language
    question: Where do I get the dubbed audio for one language once the dub is done?
  - id: getDubbedTranscript
    intent: Get a dubbed language's timed transcript
    question: Can I get the timed transcript for one language version of a dub?
  - id: getDubbingResource
    intent: Get a dub's segments, speakers and languages
    question: What segments and speakers make up a dubbing project?
  - id: translateSegment
    intent: Translate one segment of a dub
    question: Can I retranslate a single line of a dub into a target language?
  - id: dubSegment
    intent: Generate dubbed audio for one segment
    question: Can I regenerate the dubbed voice for a single translated segment?
  phrasing_ops: 5
  slug: elevenlabs-dubbing-resources-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating voice clones from short audio samples with instant processing.
  name: elevenlabs Instant Voice Cloning API
  phrasing_intents:
  - id: createInstantVoiceClone
    intent: Clone a voice instantly from samples
    question: Can I clone my own voice from a few short audio clips?
  phrasing_ops: 1
  slug: elevenlabs-instant-voice-cloning-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing knowledge base documents that agents use to answer questions.
  name: elevenlabs Knowledge Base API
  phrasing_intents:
  - id: listKnowledgeBase
    intent: List knowledge base documents
    question: Which documents are in my agents' knowledge base?
  - id: addKnowledgeBaseDocument
    intent: Add a document to the knowledge base
    question: How do I give my voice agent a PDF to answer questions from?
  - id: deleteKnowledgeBaseDocument
    intent: Delete a knowledge base document
    question: How do I remove an outdated document from the knowledge base?
  - id: getDependentAgents
    intent: See which agents use a knowledge base document
    question: Which agents depend on this knowledge base document?
  phrasing_ops: 4
  slug: elevenlabs-knowledge-base-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for generating music from text prompts using AI models.
  name: elevenlabs Music Generation API
  phrasing_intents:
  - id: compose_plan
    intent: Draft a composition plan for a song
    question: Can I get a section-by-section plan for a song before generating audio?
  - id: generate
    intent: Generate a song from a text prompt
    question: Can ElevenLabs make an original song from a description of the mood and genre?
  - id: compose_detailed
    intent: Compose a song with timestamps and metadata
    question: Can I get word timestamps and a waveform along with a composed song?
  - id: compose_detailed_stream
    intent: Stream a song with metadata over SSE
    question: Can I receive a song and its timestamps as server-sent events while it generates?
  - id: stream_compose
    intent: Stream composed music audio
    question: How do I start playing a generated song before it finishes composing?
  - id: upload_song
    intent: Upload a song for later inpainting
    question: Can I upload my own track so I can edit parts of it later?
  - id: separate_song_stems
    intent: Split a song into separate stems
    question: Can I separate vocals, drums and other instruments from a track?
  phrasing_ops: 7
  slug: elevenlabs-music-generation-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for creating high-fidelity voice clones from longer audio recordings with professional-grade processing.
  name: elevenlabs Professional Voice Cloning API
  phrasing_intents:
  - id: createProfessionalVoiceClone
    intent: Start a professional voice clone
    question: How much recorded audio do I need for a professional voice clone?
  phrasing_ops: 1
  slug: elevenlabs-professional-voice-cloning-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting speech from one voice to another while preserving the original speech characteristics.
  name: elevenlabs Speech to Speech API
  phrasing_intents:
  - id: speech_to_speech_full
    intent: Change the voice in an audio recording
    question: Can I make my recording sound like a different voice while keeping the delivery?
  - id: speech_to_speech_stream
    intent: Stream voice-changed audio
    question: Can the voice changer stream its output for real-time playback?
  phrasing_ops: 2
  slug: elevenlabs-speech-to-speech-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting audio into text transcriptions with support for multiple languages and audio formats.
  name: elevenlabs Speech to Text API
  phrasing_intents:
  - id: speech_to_text
    intent: Transcribe an audio file to text
    question: Can ElevenLabs transcribe an MP3 and give me word-level timestamps?
  - id: get_transcript_by_id
    intent: Get a transcript by ID
    question: Where do I fetch the result of a transcription I submitted earlier?
  - id: delete_transcript_by_id
    intent: Delete a transcript
    question: How do I delete a stored transcript?
  - id: convertSpeechToTextAsync
    intent: Transcribe audio in the background
    question: How do I transcribe a long recording without waiting on the request?
  phrasing_ops: 4
  slug: elevenlabs-speech-to-text-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting text scripts with multiple speakers into dialogue audio.
  name: elevenlabs Text to Dialogue API
  phrasing_intents:
  - id: text_to_dialogue
    intent: Generate multi-speaker dialogue audio
    question: How do I create a conversation between two voices from a script?
  - id: text_to_dialogue_stream
    intent: Stream multi-voice dialogue audio
    question: Can I stream a multi-voice dialogue instead of waiting for the full file?
  - id: text_to_dialogue_stream_with_timestamps
    intent: Stream dialogue audio with timestamps
    question: Can I stream dialogue as base64 audio chunks with timestamps?
  - id: text_to_dialogue_full_with_timestamps
    intent: Generate dialogue audio with word timings
    question: Can I get word-level timing for a multi-speaker dialogue?
  phrasing_ops: 4
  slug: elevenlabs-text-to-dialogue-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for converting text into speech audio with configurable voice, model, and output format settings.
  name: elevenlabs Text to Speech API
  phrasing_intents:
  - id: create_text_to_speech_generation
    intent: Queue an asynchronous speech generation job
    question: Is there an asynchronous alternative to generating speech in a single request?
  - id: list_text_to_speech_generations
    intent: List queued asynchronous speech generations
    question: Where can I see the asynchronous speech generation jobs I've queued?
  - id: get_text_to_speech_generation
    intent: Get a queued speech generation's result
    question: Has my queued speech job finished, and where's its output?
  - id: text_to_speech_full
    intent: Convert text to speech in one response
    question: How do I turn a paragraph of text into an MP3 with a specific voice?
  - id: text_to_speech_full_with_timestamps
    intent: Generate speech with word-level timings
    question: How can I highlight words on screen in sync with generated speech?
  - id: text_to_speech_stream
    intent: Stream text-to-speech audio for low latency
    question: What's the best way to start playing speech before the whole clip is generated?
  - id: text_to_speech_stream_with_timestamps
    intent: Stream speech with word-level timings
    question: Can I stream audio and get word timestamps at the same time?
  phrasing_ops: 7
  slug: elevenlabs-text-to-speech-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing external tools and webhook integrations that agents can invoke during conversations.
  name: elevenlabs Tools API
  phrasing_intents:
  - id: listTools
    intent: List tools available to agents
    question: Which webhook and MCP tools have I set up for my agents?
  - id: createTool
    intent: Create a tool agents can call
    question: How do I let my voice agent call my own API during a conversation?
  - id: deleteTool
    intent: Delete an agent tool
    question: How do I remove a tool my agents should no longer use?
  phrasing_ops: 3
  slug: elevenlabs-tools-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for browsing and adding shared voices from the public voice library.
  name: elevenlabs Voice Library API
  phrasing_intents:
  - id: listSharedVoices
    intent: Browse the public voice library
    question: What voices are in the public voice library that I could add?
  - id: addSharedVoice
    intent: Add a public library voice to my voices
    question: How do I add a voice from the public library to my own collection?
  phrasing_ops: 2
  slug: elevenlabs-voice-library-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing voice-specific settings such as stability, similarity boost, and style parameters.
  name: elevenlabs Voice Settings API
  phrasing_intents:
  - id: getVoiceSettings
    intent: Get one voice's settings
    question: What stability and similarity boost does this voice use right now?
  - id: editVoiceSettings
    intent: Change a voice's default settings
    question: How do I make a voice less monotone by default?
  - id: getDefaultVoiceSettings
    intent: Get the default voice settings
    question: What settings apply when neither the voice nor the request sets any?
  phrasing_ops: 3
  slug: elevenlabs-voice-settings-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints for managing voices including listing, creating, editing, and deleting voices in the library.
  name: elevenlabs Voices API
  phrasing_intents:
  - id: get_voice_settings_default
    intent: Get the default voice settings
    question: What stability and similarity values do voices use by default?
  - id: get_voice_settings
    intent: Get the settings of one voice
    question: What stability and style is a particular voice currently set to?
  - id: edit_voice_settings
    intent: Change a voice's stability, style or speed
    question: How do I make a voice sound more stable or more expressive?
  - id: get_voice_accents
    intent: List accents in the shared voice library
    question: What accents can I filter shared voices by?
  - id: get_voices
    intent: List all voices available to me
    question: Which voices can I use for text to speech in ElevenLabs?
  - id: get_voice_by_id
    intent: Get a voice's details
    question: What labels, samples and description does a particular voice have?
  - id: delete_voice
    intent: Delete a voice from my library
    question: How do I delete a custom voice I made?
  - id: edit_voice
    intent: Rename or relabel a voice and add samples
    question: Can I rename one of my voices or change its description?
  phrasing_ops: 14
  slug: elevenlabs-voices-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints accessible to all authenticated callers regardless of scope.
  name: ElevenLabs Access:all API
  phrasing_intents:
  - id: usage_by_product_over_time
    intent: Chart workspace credit usage by product
    question: How many credits has each product used in my workspace over time?
  - id: requests_list
    intent: List API requests made by the workspace
    question: Can I see a log of individual API requests my workspace made?
  phrasing_ops: 2
  slug: elevenlabs-access-all-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Query analytics and insights about agent conversations and performance.
  name: ElevenLabs Agents Insights API
  phrasing_intents:
  - id: get_agent_topics_route
    intent: See what topics an agent's conversations cover
    question: What are callers talking to my agent about most?
  phrasing_ops: 1
  slug: elevenlabs-agents-insights-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Build, configure and manage Conversational AI agents, knowledge bases, tools, and conversations.
  name: ElevenLabs Agents Platform API
  phrasing_intents:
  - id: get_conversation_signed_link
    intent: Get a signed URL to talk to a private agent
    question: How do I start a conversation with an agent that requires authorization?
  - id: get_signed_url_deprecated
    intent: Get a signed agent URL via the legacy endpoint
    question: Is the underscore get_signed_url path still usable for private agents?
  - id: get_livekit_token
    intent: Get a WebRTC token for a live agent session
    question: How can my app open a real-time WebRTC voice session with an agent?
  - id: handle_twilio_outbound_call
    intent: Place an outbound agent call through Twilio
    question: How do I have my voice agent dial a customer using a Twilio number?
  - id: register_twilio_call
    intent: Register a Twilio call and get TwiML back
    question: What TwiML do I return to connect a Twilio call I manage myself to an agent?
  - id: handle_exotel_outbound_call
    intent: Place an outbound agent call through Exotel
    question: How can my agent dial out using an Exotel phone number?
  - id: whatsapp_outbound_call
    intent: Place an outbound agent voice call on WhatsApp
    question: Can my agent call a customer over WhatsApp voice?
  - id: whatsapp_outbound_message
    intent: Send a WhatsApp template message from an agent
    question: How do I have an agent start a WhatsApp chat with a template message?
  phrasing_ops: 150
  slug: elevenlabs-agents-platform-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Workspace-level analytics for Conversational AI usage.
  name: ElevenLabs Agents Workspace Analytics API
  phrasing_intents:
  - id: run_conversation_analysis
    intent: Re-run analysis on a conversation
    question: I changed my agent's evaluation criteria; can I re-analyze an old conversation?
  - id: run_conversation_evaluations
    intent: Re-run one evaluation on a conversation
    question: Can I rerun just a single evaluation criterion on a conversation?
  phrasing_ops: 2
  slug: elevenlabs-agents-workspace-analytics-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Manage API keys for your workspace.
  name: ElevenLabs API Key API
  phrasing_intents:
  - id: disable
    intent: Disable the API key making this request
    question: How do I shut off an API key that I think has leaked, using the key itself?
  - id: set_third_party_disabling_policy
    intent: Set whether found keys can be disabled by anyone
    question: Can I stop third parties who find one of our keys from disabling it?
  phrasing_ops: 2
  slug: elevenlabs-api-key-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The Assets API from ElevenLabs — 2 operation(s) for assets.
  name: ElevenLabs Assets API
  phrasing_intents:
  - id: upload_asset
    intent: Upload an asset
    question: How do I upload a file as a workspace asset?
  - id: list_assets
    intent: List workspace assets
    question: Which assets have been uploaded to my workspace?
  - id: get_asset
    intent: Get an asset by ID
    question: How do I fetch a single asset's details?
  - id: delete_asset_endpoint
    intent: Delete an asset
    question: Can I remove an asset I no longer need?
  phrasing_ops: 4
  slug: elevenlabs-assets-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The Convai API from ElevenLabs — 14 operation(s) for convai.
  name: ElevenLabs Convai API
  phrasing_intents:
  - id: create_agent_response_test_route
    intent: Create an agent response test
    question: How do I write a test that checks how my voice agent responds?
  - id: get_agent_response_test_route
    intent: Get an agent response test
    question: What does one of my saved agent response tests check for?
  - id: update_agent_response_test_route
    intent: Update an agent response test
    question: Can I change the expected behavior in an existing agent response test?
  - id: delete_chat_response_test_route
    intent: Delete an agent response test
    question: How do I get rid of an agent response test I no longer need?
  - id: get_agent_response_tests_summaries_route
    intent: Get summaries for several agent tests
    question: Can I fetch short summaries of several agent tests in one request?
  - id: list_chat_response_tests_route
    intent: List agent response tests
    question: Which agent response tests have I created so far?
  - id: list_test_invocations_route
    intent: List agent test runs
    question: When were tests last run against my agent and how did they go?
  - id: run_agent_test_suite_route
    intent: Run tests against an agent
    question: How do I run my saved tests against a voice agent before shipping a change?
  phrasing_ops: 20
  slug: elevenlabs-convai-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Build and manage conversational AI agents (legacy tag — see also Agents Platform).
  name: ElevenLabs Conversational AI API
  phrasing_intents:
  - id: create_crawl_job_route
    intent: Crawl a website into the knowledge base
    question: How do I import a whole documentation site into my agent's knowledge base?
  - id: list_crawl_jobs_route
    intent: List recent knowledge base crawl jobs
    question: Which website crawl jobs are running or recently finished for my agents' knowledge base?
  - id: get_crawl_job_route
    intent: Check a crawl job's progress
    question: How far along is my knowledge base crawl?
  - id: cancel_crawl_job_route
    intent: Cancel a crawl job and discard its documents
    question: Can I stop a crawl that is pulling in the wrong pages?
  - id: create_folder_route
    intent: Create a knowledge base folder
    question: Can I organize knowledge base documents into folders?
  - id: post_knowledge_base_move_route
    intent: Move one knowledge base document to a folder
    question: How do I move a single document into another knowledge base folder?
  - id: post_knowledge_base_bulk_move_route
    intent: Move many knowledge base items at once
    question: Can I move a batch of documents and folders together?
  phrasing_ops: 7
  slug: elevenlabs-conversational-ai-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The Docs API from ElevenLabs — 1 operation(s) for docs.
  name: ElevenLabs Docs API
  phrasing_intents:
  - id: redirect_to_mintlify
    intent: Open the API documentation
    question: Where is the ElevenLabs API reference hosted?
  phrasing_ops: 1
  slug: elevenlabs-docs-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Endpoints available only to enterprise workspaces.
  name: ElevenLabs Enterprise API
  phrasing_intents:
  - id: get_dubbing_resource
    intent: Get a Studio-enabled dubbing resource
    question: How do I see the speakers, segments and languages inside a dubbing project?
  - id: add_language
    intent: Add a target language to a dubbing resource
    question: Can I add another target language to an existing dub?
  - id: create_clip
    intent: Create a new segment for a dubbing speaker
    question: How do I add a new timed segment for a speaker in my dub?
  - id: update_segment_language
    intent: Edit one segment's text or timing in a language
    question: Can I fix the translated text of a single segment for just one language?
  - id: migrate_segments
    intent: Reassign dubbing segments to another speaker
    question: A few lines were attributed to the wrong speaker; can I move them?
  - id: delete_segment
    intent: Delete a segment from a dub
    question: How do I remove an unwanted segment from a dubbing project?
  - id: transcribe
    intent: Re-transcribe selected dubbing segments
    question: Can I regenerate the source transcript for specific segments of a dub?
  - id: translate
    intent: Regenerate translations for dubbing segments
    question: How do I redo the translation for some segments in certain languages?
  phrasing_ops: 13
  slug: elevenlabs-enterprise-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The Flows API from ElevenLabs — 6 operation(s) for flows.
  name: ElevenLabs Flows API
  phrasing_intents:
  - id: create_video_generation
    intent: Start a video generation
    question: How do I generate a video with one of the Flows models?
  - id: list_video_generations
    intent: List my video generations
    question: Which AI video generations have I started through the API?
  - id: get_video_generation
    intent: Check a video generation and get its URL
    question: Is my video generation finished yet?
  - id: create_image_generation
    intent: Start an image generation
    question: Can I create images with ElevenLabs Flows?
  - id: list_image_generations
    intent: List my image generations
    question: What images have I generated through the Flows API?
  - id: get_image_generation
    intent: Check an image generation and get its URL
    question: Has my image generation completed?
  - id: create_text_to_speech_generation
    intent: Start an asynchronous speech generation
    question: When should I use the asynchronous Flows speech generation instead of direct text-to-speech?
  - id: list_text_to_speech_generations
    intent: List my asynchronous speech generations
    question: Which asynchronous speech generations have I started through Flows?
  phrasing_ops: 9
  slug: elevenlabs-flows-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Force align an audio file to a text transcript to get precise word-level and character level timing information. Response is a list of characters with their start and end times as milliseconds elapsed
  name: ElevenLabs Forced Alignment API
  phrasing_intents:
  - id: forced_alignment
    intent: Align a transcript to audio timing
    question: Can I get word-by-word timings for audio when I already have the transcript?
  phrasing_ops: 1
  slug: elevenlabs-forced-alignment-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The Image API from ElevenLabs — 2 operation(s) for image.
  name: ElevenLabs Image API
  phrasing_intents:
  - id: create_image_generation
    intent: Start an image generation
    question: Can ElevenLabs generate images as well as audio?
  - id: list_image_generations
    intent: List my image generations
    question: What images have I generated through the API?
  - id: get_image_generation
    intent: Check an image generation and get its output
    question: Is my image finished generating yet?
  phrasing_ops: 3
  slug: elevenlabs-image-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Access the different models of the platform.
  name: ElevenLabs Models API
  phrasing_intents:
  - id: get_models
    intent: List available voice models
    question: Which ElevenLabs models can I use for speech generation?
  phrasing_ops: 1
  slug: elevenlabs-models-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Create and manage music finetunes.
  name: ElevenLabs Music Finetunes API
  phrasing_intents:
  - id: get_finetunes
    intent: List music finetunes I can use
    question: Which music finetunes can I use, including ones shared by my workspace?
  - id: create_finetune
    intent: Create a music finetune
    question: How do I train a custom music style on my own audio tracks?
  - id: get_finetune
    intent: Get a music finetune
    question: How do I check the details of one music finetune?
  - id: update_finetune
    intent: Update a music finetune
    question: Can I rename a finetune or replace its tags?
  - id: delete_finetune
    intent: Delete a music finetune
    question: Can I permanently delete a music finetune I made?
  phrasing_ops: 5
  slug: elevenlabs-music-finetunes-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Access and manage ElevenProductions orders.
  name: ElevenLabs Productions API
  phrasing_intents:
  - id: public_create_order
    intent: Start a new Productions order
    question: How do I start an order for human-reviewed Productions work?
  - id: public_list_orders
    intent: List Productions orders
    question: What Productions orders has my workspace placed?
  - id: public_get_order
    intent: Get a Productions order and its quote
    question: What's the quoted price on my Productions order?
  - id: public_update_order
    intent: Update an open Productions order
    question: Can I change a Productions order before I submit it?
  - id: public_register_media
    intent: Attach a media file to a Productions order
    question: How do I attach my video to a Productions order?
  - id: public_get_media_info
    intent: Get an order's uploaded media and download link
    question: Can I re-download a media file I attached to an order?
  - id: public_upsert_order_item
    intent: Add or change an item on an order
    question: How do I add a line item to my Productions order and see its price?
  - id: public_remove_order_item
    intent: Remove an item from an open order
    question: Can I take an item off a Productions order before submitting?
  phrasing_ops: 11
  slug: elevenlabs-productions-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Manage pronunciation dictionaries that override how specific words are pronounced.
  name: ElevenLabs Pronunciation Dictionary API
  phrasing_intents:
  - id: add_from_file
    intent: Create a pronunciation dictionary from a PLS file
    question: Can I import an existing PLS lexicon as a pronunciation dictionary?
  - id: add_from_rules
    intent: Create a pronunciation dictionary from rules
    question: Can I build a pronunciation dictionary by listing rules instead of uploading a file?
  - id: patch_pronunciation_dictionary
    intent: Rename or archive a pronunciation dictionary
    question: Can I archive a pronunciation dictionary I no longer use?
  - id: get_pronunciation_dictionary_metadata
    intent: Get a pronunciation dictionary's metadata
    question: What is the latest version of a pronunciation dictionary?
  - id: set_rules
    intent: Replace all rules in a pronunciation dictionary
    question: How do I overwrite every rule in a dictionary with a new set?
  - id: add_rules
    intent: Add rules to a pronunciation dictionary
    question: Can I add a few new pronunciations to an existing dictionary?
  - id: remove_rules
    intent: Remove rules from a pronunciation dictionary
    question: How do I delete specific words from a pronunciation dictionary?
  - id: get_pronunciation_dictionary_version_pls
    intent: Download a dictionary version as a PLS file
    question: Can I export a pronunciation dictionary as a PLS lexicon?
  phrasing_ops: 9
  slug: elevenlabs-pronunciation-dictionary-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Create and manage Professional Voice Clones (PVCs).
  name: ElevenLabs Pvc Voices API
  phrasing_intents:
  - id: create_pvc_voice
    intent: Create a Professional Voice Clone
    question: How do I start a professional voice clone before uploading any samples?
  - id: edit_pvc_voice
    intent: Edit a PVC voice's metadata
    question: Can I rename a professional voice clone or change its language?
  - id: add_pvc_voice_samples
    intent: Upload audio samples to a PVC voice
    question: How do I upload training recordings for a professional voice clone?
  - id: edit_pvc_voice_sample
    intent: Trim or clean up a PVC voice sample
    question: Can I trim the start and end of a sample used for PVC training?
  - id: delete_pvc_voice_sample
    intent: Delete a sample from a PVC voice
    question: How do I remove a bad recording from my professional voice clone?
  - id: get_pvc_sample_audio
    intent: Preview a PVC sample's audio
    question: Can I listen to a PVC sample with background noise removed?
  - id: get_pvc_sample_visual_waveform
    intent: Get a PVC sample's waveform
    question: Can I get a visual waveform of a voice sample to show in my UI?
  - id: get_pvc_sample_speakers
    intent: Check speaker separation status for a sample
    question: Has speaker separation finished for my PVC sample?
  phrasing_ops: 14
  slug: elevenlabs-pvc-voices-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Manage dubbing resources, including segments, speakers, and language tracks.
  name: ElevenLabs Resource API
  phrasing_intents:
  - id: get_dubbing_resource
    intent: Get a Dubbing Studio resource
    question: How do I load the Dubbing Studio resource for a studio-enabled dub?
  - id: add_language
    intent: Add a language to a Dubbing Studio resource
    question: Can I add another language to a studio dub without generating audio right away?
  - id: create_clip
    intent: Create a segment for a speaker in a studio dub
    question: How do I add a new timed segment for one speaker in Dubbing Studio?
  - id: update_segment_language
    intent: Edit a studio segment for one language
    question: Can I change a studio segment's text in just one language?
  - id: migrate_segments
    intent: Move segments to a different speaker
    question: The dub attributed lines to the wrong person, how do I reassign them?
  - id: delete_segment
    intent: Delete a segment from a studio dub
    question: How do I delete an unwanted segment in Dubbing Studio?
  - id: transcribe
    intent: Re-transcribe segments in a studio dub
    question: Can I redo the transcription of specific segments in Dubbing Studio?
  - id: translate
    intent: Regenerate translations in a studio dub
    question: How do I refresh the translations for some segments and languages in Dubbing Studio?
  phrasing_ops: 13
  slug: elevenlabs-resource-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Access to your samples. A sample is any audio file you attached to a voice. A voice can have one or more samples.
  name: ElevenLabs Samples API
  phrasing_intents:
  - id: delete_sample
    intent: Delete a sample from a voice
    question: How do I remove a bad recording from one of my cloned voices?
  - id: get_audio_from_sample
    intent: Play a voice sample's audio
    question: Can I listen to a sample I uploaded for a voice?
  phrasing_ops: 2
  slug: elevenlabs-samples-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Manage individual segments within a dubbing resource.
  name: ElevenLabs Segment API
  phrasing_intents:
  - id: get_dubbing_resource
    intent: Fetch a dubbing resource by ID
    question: What's inside my dubbing resource right now?
  - id: add_language
    intent: Add a language to a dub
    question: Can I extend an existing dub with one more language?
  - id: create_clip
    intent: Add a timed segment for a speaker
    question: Can I insert a new clip for a speaker between two timestamps?
  - id: update_segment_language
    intent: Modify a segment for one language
    question: How do I correct a single line of dubbed text in one target language?
  - id: migrate_segments
    intent: Move segments between speakers
    question: Can I transfer segments from one speaker to another in a dub?
  - id: delete_segment
    intent: Remove a single dubbing segment
    question: Is there a way to drop one segment from a dub entirely?
  - id: transcribe
    intent: Transcribe specific segments again
    question: The source transcript for some segments is wrong; can I redo just those?
  - id: translate
    intent: Translate some or all segments again
    question: Can I retranslate a dub into just two of its languages?
  phrasing_ops: 13
  slug: elevenlabs-segment-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Mint short-lived, single-use tokens for client-side use of Conversational AI agents.
  name: ElevenLabs Single Use Token API
  phrasing_intents:
  - id: get_single_use_token
    intent: Create a single-use token for a frontend
    question: How do I let a browser client call the API without exposing my key?
  phrasing_ops: 1
  slug: elevenlabs-single-use-token-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Generate sound effects and non-speech audio from a text prompt.
  name: ElevenLabs Sound Generation API
  phrasing_intents:
  - id: sound_generation
    intent: Generate a sound effect from text
    question: Can I create a sound effect just by describing it?
  phrasing_ops: 1
  slug: elevenlabs-sound-generation-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Low-latency, real-time speech generation endpoints.
  name: ElevenLabs Speech Engine API
  phrasing_intents:
  - id: list_speech_engines
    intent: List Speech Engines
    question: Which Speech Engine resources have I configured?
  - id: create_speech_engine
    intent: Create a Speech Engine
    question: How do I set up a Speech Engine with my own speech recognition and TTS settings?
  - id: get_speech_engine
    intent: Get a Speech Engine
    question: How is a particular Speech Engine configured?
  - id: update_speech_engine
    intent: Update a Speech Engine's settings
    question: Can I change just the TTS settings of an existing Speech Engine?
  - id: delete_speech_engine
    intent: Delete a Speech Engine
    question: How do I remove a Speech Engine I no longer need?
  phrasing_ops: 5
  slug: elevenlabs-speech-engine-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Accesses your speech history. Your speech history is a list of all your created audio including its metadata using our text-to-speech and speech-to-speech models.
  name: ElevenLabs Speech History API
  phrasing_intents:
  - id: get_speech_history
    intent: Browse my generated audio history
    question: Where can I find all the audio I've generated before?
  - id: get_speech_history_item_by_id
    intent: Get one history item's details
    question: What text, voice and settings were used for a past generation?
  - id: delete_speech_history_item
    intent: Delete a history item
    question: How do I remove a generation from my history?
  - id: get_audio_full_from_speech_history_item
    intent: Play back audio from a history item
    question: Can I re-download the audio of something I generated earlier?
  - id: download_speech_history_items
    intent: Download several history items as files
    question: Can I download multiple past generations in one zip file?
  phrasing_ops: 5
  slug: elevenlabs-speech-history-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Access, create and convert Studio Projects programmatically. Only specifically whitelisted accounts can access the Studio API. If you need access please contact our sales team.
  name: ElevenLabs Studio API
  phrasing_intents:
  - id: create_podcast
    intent: Generate a podcast from source content
    question: Can ElevenLabs turn an article or document into a two-host podcast automatically?
  - id: update_pronunciation_dictionaries
    intent: Attach pronunciation dictionaries to a Studio project
    question: How do I make a Studio project pronounce names consistently using a pronunciation dictionary?
  - id: get_projects
    intent: List my Studio projects
    question: What Studio projects do I have?
  - id: add_project
    intent: Create a Studio project
    question: How do I start a new audiobook project in Studio from an EPUB or PDF?
  - id: edit_project
    intent: Update a Studio project's settings
    question: Can I rename a Studio project or change its default voices?
  - id: get_project_by_id
    intent: Get a Studio project's details
    question: How do I see the full details of one Studio project?
  - id: delete_project
    intent: Delete a Studio project
    question: How do I permanently remove a Studio project I no longer need?
  - id: edit_project_content
    intent: Replace a Studio project's content
    question: Can I swap the text of an existing Studio project with a new document?
  phrasing_ops: 23
  slug: elevenlabs-studio-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Design and generate custom voices from a text prompt.
  name: ElevenLabs Text To Voice API
  phrasing_intents:
  - id: text_to_voice
    intent: Generate voice previews (deprecated endpoint)
    question: Can I still use the older create-previews endpoint to generate voices from a description?
  - id: create_voice
    intent: Save a generated voice preview as a voice
    question: I like one of the designed voice previews, how do I keep it?
  - id: text_to_voice_design
    intent: Design a new voice from a text prompt
    question: Can I describe a voice in words and get samples of it?
  - id: text_to_voice_remix
    intent: Remix an existing voice with a prompt
    question: Can I make one of my voices sound older or calmer by describing the change?
  - id: text_to_voice_preview_stream
    intent: Stream a designed voice preview
    question: Can I stream the audio of a voice preview instead of decoding base64?
  phrasing_ops: 5
  slug: elevenlabs-text-to-voice-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The Usage API from ElevenLabs — 1 operation(s) for usage.
  name: ElevenLabs Usage API
  phrasing_intents:
  - id: usage_characters
    intent: Get character usage over time (deprecated)
    question: How many characters did I use each day over a date range?
  phrasing_ops: 1
  slug: elevenlabs-usage-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The User API from ElevenLabs — 2 operation(s) for user.
  name: ElevenLabs User API
  phrasing_intents:
  - id: get_user_info
    intent: Get my account profile
    question: What account details does the API return about me?
  - id: get_user_subscription_info
    intent: Get my subscription details
    question: Which subscription tier am I on and how much of my quota is left?
  phrasing_ops: 2
  slug: elevenlabs-user-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: The Video API from ElevenLabs — 2 operation(s) for video.
  name: ElevenLabs Video API
  phrasing_intents:
  - id: create_video_generation
    intent: Start a new video generation
    question: How do I kick off generating a video from the API?
  - id: list_video_generations
    intent: List my video generations
    question: Which video generations have I started, with the newest first?
  - id: get_video_generation
    intent: Check a video generation's status and output
    question: Is my video generation finished yet?
  phrasing_ops: 3
  slug: elevenlabs-video-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Generate music that matches the content and mood of a video.
  name: ElevenLabs Video To Music API
  phrasing_intents:
  - id: video_to_music
    intent: Generate background music for a video
    question: Can I get a soundtrack generated to fit my video clips?
  phrasing_ops: 1
  slug: elevenlabs-video-to-music-api
- baseURL: https://api.elevenlabs.io
  baseurl_source: declared
  description: Access to workspace related endpoints.
  name: ElevenLabs Workspace API
  phrasing_intents:
  - id: disable
    intent: Disable the API key making this request
    question: How can I switch off the very API key I'm calling with if I think it leaked?
  - id: set_third_party_disabling_policy
    intent: Set the workspace third-party key disabling policy
    question: Can I force every API key in my workspace to be disable-able by whoever holds it?
  - id: get_service_account_api_keys_route
    intent: List a service account's API keys
    question: Which API keys belong to a given service account?
  - id: create_service_account_api_key
    intent: Create an API key for a service account
    question: How do I issue a new API key for a service account?
  - id: edit_service_account_api_key
    intent: Update a service account's API key
    question: Can I temporarily disable a service account key instead of deleting it?
  - id: delete_service_account_api_key
    intent: Delete a service account's API key
    question: How do I permanently remove an API key from a service account?
  - id: get_workspace_audit_logs
    intent: Read the workspace audit log
    question: Where can I see who changed what in my workspace?
  - id: create_auth_connection
    intent: Create a workspace OAuth2 auth connection
    question: How do I add a new OAuth2 auth connection to my workspace?
  phrasing_ops: 29
  slug: elevenlabs-workspace-api
artifact_total: 192
asyncapis:
- description: The ElevenLabs Conversational AI WebSocket API enables real-time, interactive voice conversations with AI agents. It supports bidirectional audio streaming, text events, and conversation lifecycle man
  name: ElevenLabs Conversational AI Events
  slug: elevenlabs-conversational-ai-asyncapi
- description: The ElevenLabs Text to Speech WebSocket API enables bidirectional streaming for text-to-speech conversion. Clients send text chunks incrementally and receive audio chunks as they are generated, enabli
  name: ElevenLabs Text to Speech Streaming Events
  slug: elevenlabs-text-to-speech-streaming-asyncapi
- description: The ElevenLabs Webhook system delivers event notifications to configured endpoints when specific actions occur within the platform. This includes post-call webhooks from Conversational AI conversation
  name: ElevenLabs Webhook Events
  slug: elevenlabs-webhooks-asyncapi
collections:
- collection_type: open
  name: ElevenLabs Audio Isolation Agents API
  slug: open-elevenlabs-agents-api
- collection_type: open
  name: ElevenLabs Agents Audio Isolation API
  slug: open-elevenlabs-audio-isolation-api
- collection_type: open
  name: ElevenLabs Audio Isolation API
  slug: open-elevenlabs-audio-isolation
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Audio Native API
  slug: open-elevenlabs-audio-native-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Chapters API
  slug: open-elevenlabs-chapters-api
- collection_type: open
  name: ElevenLabs Conversational AI API
  slug: open-elevenlabs-conversational-ai
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Conversations API
  slug: open-elevenlabs-conversations-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Dubbing API
  slug: open-elevenlabs-dubbing-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Dubbing Resources API
  slug: open-elevenlabs-dubbing-resources-api
- collection_type: open
  name: ElevenLabs Dubbing API
  slug: open-elevenlabs-dubbing
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Instant Voice Cloning API
  slug: open-elevenlabs-instant-voice-cloning-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Knowledge Base API
  slug: open-elevenlabs-knowledge-base-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Music Generation API
  slug: open-elevenlabs-music-generation-api
- collection_type: open
  name: ElevenLabs Music Generation API
  slug: open-elevenlabs-music
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Professional Voice Cloning API
  slug: open-elevenlabs-professional-voice-cloning-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Projects API
  slug: open-elevenlabs-projects-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Pronunciation Dictionaries API
  slug: open-elevenlabs-pronunciation-dictionaries-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Sound Effects API
  slug: open-elevenlabs-sound-effects-api
- collection_type: open
  name: ElevenLabs Sound Effects API
  slug: open-elevenlabs-sound-effects
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Speech to Speech API
  slug: open-elevenlabs-speech-to-speech-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Speech to Text API
  slug: open-elevenlabs-speech-to-text-api
- collection_type: open
  name: ElevenLabs Speech to Text API
  slug: open-elevenlabs-speech-to-text
- collection_type: open
  name: ElevenLabs Studio API
  slug: open-elevenlabs-studio
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Text to Dialogue API
  slug: open-elevenlabs-text-to-dialogue-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Text to Speech API
  slug: open-elevenlabs-text-to-speech-api
- collection_type: open
  name: ElevenLabs Text to Speech API
  slug: open-elevenlabs-text-to-speech
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Tools API
  slug: open-elevenlabs-tools-api
- collection_type: open
  name: ElevenLabs Voice Changer API
  slug: open-elevenlabs-voice-changer
- collection_type: open
  name: ElevenLabs Voice Cloning API
  slug: open-elevenlabs-voice-cloning
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Voice Library API
  slug: open-elevenlabs-voice-library-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Voice Settings API
  slug: open-elevenlabs-voice-settings-api
- collection_type: open
  name: ElevenLabs Audio Isolation Agents Voices API
  slug: open-elevenlabs-voices-api
- collection_type: open
  name: ElevenLabs Voices API
  slug: open-elevenlabs-voices
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://elevenlabs.io/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/elevenlabs/capabilities/elevenlabs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/elevenlabs-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.elevenlabs.io/
- group: agent
  href: https://artifacts.apis.io/elevenlabs/agentic-access/elevenlabs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elevenlabs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/elevenlabs/security/elevenlabs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elevenlabs-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/elevenlabs/security/elevenlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elevenlabs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/elevenlabs/authentication/elevenlabs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elevenlabs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elevenlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elevenlabsio
- group: company
  title: ''
  type: Blog
  url: https://elevenlabs.io/blog
- group: design
  href: https://artifacts.apis.io/elevenlabs/json-ld/elevenlabs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/elevenlabs-context.jsonld
- group: docs
  href: https://artifacts.apis.io/elevenlabs/json-schema/elevenlabs-voice-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-voice-schema.json
- group: docs
  href: https://artifacts.apis.io/elevenlabs/json-schema/elevenlabs-agent-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-agent-schema.json
- group: docs
  href: https://artifacts.apis.io/elevenlabs/json-schema/elevenlabs-webhook-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/elevenlabs-webhook-event-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://elevenlabs.io/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://elevenlabs.io/docs/overview/intro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://elevenlabs.io/api
- group: docs
  title: ''
  type: APIReference
  url: https://elevenlabs.io/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://elevenlabs.io/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://elevenlabs.io/docs/help-center/help-center-directory
- group: commercial
  title: ''
  type: Pricing
  url: https://elevenlabs.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://elevenlabs.io/app/sign-up
- group: start
  title: ''
  type: Login
  url: https://elevenlabs.io/app/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elevenlabs.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elevenlabs.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elevenlabs.io/
- group: design
  href: https://artifacts.apis.io/elevenlabs/lifecycle/elevenlabs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elevenlabs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/elevenlabs/lifecycle/elevenlabs-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/elevenlabs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/elevenlabs/changelog/elevenlabs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elevenlabs-changelog.yml
- group: auth
  href: https://artifacts.apis.io/elevenlabs/security/elevenlabs-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/elevenlabs-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/elevenlabs/well-known/elevenlabs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elevenlabs-security.txt
- group: agent
  href: https://artifacts.apis.io/elevenlabs/well-known/elevenlabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elevenlabs-well-known.yml
- group: other
  href: https://artifacts.apis.io/elevenlabs/well-known/elevenlabs-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/elevenlabs-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/elevenlabs/security/elevenlabs-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elevenlabs-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/elevenlabs/conformance/elevenlabs-conformance.yml
  title: ''
  type: Compliance
  url: conformance/elevenlabs-conformance.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/conformance/elevenlabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elevenlabs-conformance.yml
- group: build
  href: https://artifacts.apis.io/elevenlabs/packages/elevenlabs-packages.yml
  title: ''
  type: Packages
  url: packages/elevenlabs-packages.yml
- group: build
  href: https://artifacts.apis.io/elevenlabs/packages/elevenlabs-packages.yml
  title: ''
  type: SDKs
  url: packages/elevenlabs-packages.yml
- group: build
  href: https://artifacts.apis.io/elevenlabs/cli/elevenlabs-cli.yml
  title: ''
  type: CLI
  url: cli/elevenlabs-cli.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/components/elevenlabs-components.yml
  title: ''
  type: Components
  url: components/elevenlabs-components.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/data-model/elevenlabs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elevenlabs-data-model.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/conventions/elevenlabs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elevenlabs-conventions.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/errors/elevenlabs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elevenlabs-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/elevenlabs/scopes/elevenlabs-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/elevenlabs-scopes.yml
- group: agent
  href: https://artifacts.apis.io/elevenlabs/mcp/elevenlabs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elevenlabs-mcp.yml
- group: build
  href: https://artifacts.apis.io/elevenlabs/mcp/elevenlabs-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/elevenlabs-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/elevenlabs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/elevenlabs/llms/elevenlabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elevenlabs-llms.txt
- group: other
  href: https://artifacts.apis.io/elevenlabs/overlays/elevenlabs-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elevenlabs-openapi-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/elevenlabs/plans/elevenlabs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elevenlabs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/elevenlabs/rate-limits/elevenlabs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elevenlabs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/elevenlabs/finops/elevenlabs-finops.yml
  title: ''
  type: FinOps
  url: finops/elevenlabs-finops.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/vocabulary/elevenlabs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/elevenlabs-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/rules/elevenlabs-asyncapi-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/elevenlabs-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/rules/elevenlabs-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/elevenlabs-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/elevenlabs/asyncapi/elevenlabs-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/elevenlabs-webhooks-asyncapi.yml
created: '2026-05-04'
description: 'ElevenLabs is an AI research and product company building voice and audio models, founded in 2022 and launched publicly in January 2023 with the first human-like AI voice model. It sells across three platforms: ElevenCreative (text to speech, speech to text, voice cloning and design, music, sound effects, dubbing, Studio, image and video across 70+ languages), ElevenAgents (an enterprise platform for voice and chat agents with telephony, testing, evaluation and analytics), and ElevenAPI (direct developer access to the audio foundation models over HTTP and WebSocket). It publishes a single first-party OpenAPI 3.1.0 covering 390 operations, official SDKs for Python, JavaScript, React, React Native, Swift, Kotlin and Flutter, a Rust CLI, a hosted remote MCP server with four data-residency endpoints, and ten Agent Skills of its own.'
features:
- 'Free: 10k credits/mo with TTS/STT/Sound effects'
- 'Starter at $6/mo: 30k credits, commercial license, IVC'
- 'Creator at $11/mo: 121k credits, Professional Voice Cloning'
- 'Pro at $99/mo: 600k credits, 44.1kHz PCM'
- 'Scale at $299/mo: 1.8M credits, team collaboration'
- 'Business at $990/mo: 6M credits, low-latency TTS at 5c/min'
- 'Enterprise custom: HIPAA BAA, SSO, custom concurrency'
- 'Concurrent: 2 Free, 3 Starter, 5 Creator, 10 Pro, 15 Scale/Business'
- TTS API with multilingual voices
- STT (Scribe) API
- Dubbing API for video translation
- Voice cloning (Instant + Professional)
- Sound Effects generation
- Music generation
- Conversational AI (voice agents)
- WebSocket streaming for low-latency synthesis
finops:
- has_sources: true
  method: derived
  name: Elevenlabs Finops
  primary_unit: subscription
  service_category: ''
  slug: elevenlabs-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elevenlabs.png
json_schemas:
- name: AddKnowledgeBaseRequest
  property_count: 3
  slug: elevenlabs-addknowledgebaserequest
- name: AddVoiceRequest
  property_count: 4
  slug: elevenlabs-addvoicerequest
- name: AddVoiceResponse
  property_count: 1
  slug: elevenlabs-addvoiceresponse
- name: ElevenLabs Conversational AI Agent
  property_count: 7
  slug: elevenlabs-agent
- name: AgentListResponse
  property_count: 3
  slug: elevenlabs-agentlistresponse
- name: AgentResponse
  property_count: 1
  slug: elevenlabs-agentresponse
- name: AgentSummary
  property_count: 3
  slug: elevenlabs-agentsummary
- name: AsyncTranscriptionResponse
  property_count: 2
  slug: elevenlabs-asynctranscriptionresponse
- name: AudioEvent
  property_count: 3
  slug: elevenlabs-audioevent
- name: AudioIsolationRequest
  property_count: 1
  slug: elevenlabs-audioisolationrequest
- name: AudioNativeResponse
  property_count: 2
  slug: elevenlabs-audionativeresponse
- name: Chapter
  property_count: 5
  slug: elevenlabs-chapter
- name: ChapterListResponse
  property_count: 1
  slug: elevenlabs-chapterlistresponse
- name: ChapterSummary
  property_count: 3
  slug: elevenlabs-chaptersummary
- name: Conversation
  property_count: 6
  slug: elevenlabs-conversation
- name: ConversationConfig
  property_count: 4
  slug: elevenlabs-conversationconfig
- name: ConversationListResponse
  property_count: 3
  slug: elevenlabs-conversationlistresponse
- name: ConversationSummary
  property_count: 5
  slug: elevenlabs-conversationsummary
- name: CreateAgentRequest
  property_count: 3
  slug: elevenlabs-createagentrequest
- name: CreateAudioNativeRequest
  property_count: 7
  slug: elevenlabs-createaudionativerequest
- name: CreateDubbingRequest
  property_count: 7
  slug: elevenlabs-createdubbingrequest
- name: CreateProjectRequest
  property_count: 5
  slug: elevenlabs-createprojectrequest
- name: CreateToolRequest
  property_count: 5
  slug: elevenlabs-createtoolrequest
- name: DialogueSegment
  property_count: 3
  slug: elevenlabs-dialoguesegment
- name: DubbingMetadata
  property_count: 6
  slug: elevenlabs-dubbingmetadata
- name: DubbingResource
  property_count: 3
  slug: elevenlabs-dubbingresource
- name: DubbingResponse
  property_count: 2
  slug: elevenlabs-dubbingresponse
- name: DubbingTranscript
  property_count: 1
  slug: elevenlabs-dubbingtranscript
- name: DubSegmentRequest
  property_count: 2
  slug: elevenlabs-dubsegmentrequest
- name: EditVoiceRequest
  property_count: 4
  slug: elevenlabs-editvoicerequest
- name: InstantVoiceCloneRequest
  property_count: 4
  slug: elevenlabs-instantvoiceclonerequest
- name: KnowledgeBaseDocument
  property_count: 4
  slug: elevenlabs-knowledgebasedocument
- name: KnowledgeBaseListResponse
  property_count: 1
  slug: elevenlabs-knowledgebaselistresponse
- name: MusicGenerationRequest
  property_count: 4
  slug: elevenlabs-musicgenerationrequest
- name: ProfessionalVoiceCloneRequest
  property_count: 2
  slug: elevenlabs-professionalvoiceclonerequest
- name: Project
  property_count: 8
  slug: elevenlabs-project
- name: ProjectListResponse
  property_count: 1
  slug: elevenlabs-projectlistresponse
- name: ProjectPronunciationRequest
  property_count: 1
  slug: elevenlabs-projectpronunciationrequest
- name: ProjectSummary
  property_count: 4
  slug: elevenlabs-projectsummary
- name: PronunciationDictionaryLocator
  property_count: 2
  slug: elevenlabs-pronunciationdictionarylocator
- name: SharedVoiceListResponse
  property_count: 3
  slug: elevenlabs-sharedvoicelistresponse
- name: SimulateConversationRequest
  property_count: 2
  slug: elevenlabs-simulateconversationrequest
- name: SimulationResult
  property_count: 2
  slug: elevenlabs-simulationresult
- name: Snapshot
  property_count: 3
  slug: elevenlabs-snapshot
- name: SnapshotListResponse
  property_count: 1
  slug: elevenlabs-snapshotlistresponse
- name: SoundEffectRequest
  property_count: 3
  slug: elevenlabs-soundeffectrequest
- name: SpeechToSpeechRequest
  property_count: 4
  slug: elevenlabs-speechtospeechrequest
- name: SpeechToTextAsyncRequest
  property_count: 4
  slug: elevenlabs-speechtotextasyncrequest
- name: SpeechToTextRequest
  property_count: 5
  slug: elevenlabs-speechtotextrequest
- name: TextToDialogueRequest
  property_count: 2
  slug: elevenlabs-texttodialoguerequest
- name: TextToSpeechRequest
  property_count: 8
  slug: elevenlabs-texttospeechrequest
- name: TimestampedAudioResponse
  property_count: 2
  slug: elevenlabs-timestampedaudioresponse
- name: Tool
  property_count: 7
  slug: elevenlabs-tool
- name: ToolListResponse
  property_count: 1
  slug: elevenlabs-toollistresponse
- name: TranscriptionResponse
  property_count: 5
  slug: elevenlabs-transcriptionresponse
- name: TranscriptionWord
  property_count: 4
  slug: elevenlabs-transcriptionword
- name: TranscriptSegment
  property_count: 4
  slug: elevenlabs-transcriptsegment
- name: TranslateSegmentRequest
  property_count: 2
  slug: elevenlabs-translatesegmentrequest
- name: UpdateAgentRequest
  property_count: 3
  slug: elevenlabs-updateagentrequest
- name: ElevenLabs Voice
  property_count: 10
  slug: elevenlabs-voice
- name: VoiceCloneResponse
  property_count: 1
  slug: elevenlabs-voicecloneresponse
- name: VoiceListResponse
  property_count: 1
  slug: elevenlabs-voicelistresponse
- name: VoiceSample
  property_count: 4
  slug: elevenlabs-voicesample
- name: VoiceSettings
  property_count: 4
  slug: elevenlabs-voicesettings
- name: ElevenLabs Webhook Event
  property_count: 2
  slug: elevenlabs-webhook-event
json_structures:
- name: Elevenlabs Structure
  property_count: 0
  slug: elevenlabs-structure
jsonld:
- class_count: 0
  name: Elevenlabs Context
  property_count: 11
  slug: elevenlabs-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.elevenlabs.io over HTTP requiring OAuth.
  name: ElevenLabs MCP Server
  slug: elevenlabs
modified: '2026-10-06'
name: ElevenLabs
nav: Providers
network: true
overview: 'ElevenLabs publishes 50 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Audio Isolation API, Audio Native API, and 47 more. Tagged areas include Artificial Intelligence, Text-to-Speech, Speech-to-Text, Voice, and Audio.


  The ElevenLabs catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  ElevenLabs'' developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 49 more developer resources.'
plans:
- name: Elevenlabs Plans Pricing
  plan_count: 7
  slug: elevenlabs-plans-pricing
- name: Elevenlabs Price Estimates
  plan_count: 0
  slug: elevenlabs-price-estimates
random_paper: 1
rate_limits:
- limit_count: 35
  name: Elevenlabs Rate Limits
  slug: elevenlabs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: ElevenLabs — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: elevenlabs-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: ElevenLabs — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: elevenlabs-jsonschema-spectral-rules
scopes:
- name: Elevenlabs Scopes
  scope_count: 7
  slug: elevenlabs-scopes
  summary_line: 7 scopes · authorization_code
score:
  band: exemplar
  composite: 83.0
  coverage:
    artifact_dirs: 37
    catalog_earned: 84.0
    catalog_earned_first_party: 24.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 62.7
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 92.1
  previous_composite: 82.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 24.0
      derived: 0
      marker_coverage: 88.0
      total: 50
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/elevenlabs/elevenlabs-2026-10-11T104115.png
security:
- kind: authentication
  name: Elevenlabs Authentication
  slug: elevenlabs-authentication
  summary_line: apiKey/oauth2/bearer · 3 schemes
- kind: domain-security
  name: Elevenlabs Domain Security
  slug: elevenlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Elevenlabs Vulnerability Disclosure
  slug: elevenlabs-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Elevenlabs Trust Center
  slug: elevenlabs-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
skill_count: 10
skills:
- name: agents
  slug: elevenlabs-agents
- name: dubbing
  slug: elevenlabs-dubbing
- name: music
  slug: elevenlabs-music
- name: setup-api-key
  slug: elevenlabs-setup-api-key
- name: sound-effects
  slug: elevenlabs-sound-effects
- name: speech-engine
  slug: elevenlabs-speech-engine
- name: speech-to-text
  slug: elevenlabs-speech-to-text
- name: text-to-speech
  slug: elevenlabs-text-to-speech
- name: voice-changer
  slug: elevenlabs-voice-changer
- name: voice-isolator
  slug: elevenlabs-voice-isolator
slug: elevenlabs
tags:
- Artificial Intelligence
- Text-to-Speech
- Speech-to-Text
- Voice
- Audio
- Machine Learning
- Conversational AI
- Agents
- Dubbing
- Music Generation
- Real-Time
- Voice AI
- Voice Agents
website: https://www.elevenlabs.io/
---
