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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 506
  human_in_the_loop: 0
  name: Apyhub Agentic Access
  operation_count: 552
  slug: apyhub-agentic-access
  summary_line: 552 operations · 506 acting
api_count: 451
apis:
- description: Classify a public JPG, PNG, or WebP URL as likely AI-generated, human, or uncertain. Returns ai_score, confidence, and source_breakdown.
  name: AI-Generated Image Detection API
  slug: anyimagedetector-detect-ai-generated-image
- description: Add text or PNG headers and footers to DOCX files, from upload or URL. Return a modified document or a downloadable URL.
  name: Apply Headers and Footers on DOCX API
  slug: apyhub-add-header-footer-to-docx
- description: Add text or PNG headers and footers to a PDF from a file or URL. Returns a modified PDF or an S3 URL for invoices, reports, and branded documents.
  name: Apply Footers on PDF API
  slug: apyhub-add-header-footer-to-pdf
- description: Detect the spoken language in an audio file or public audio URL. Returns a locale code and confidence score for routing transcription and voice workflows.
  name: AI Audio Language Detection API
  slug: apyhub-ai-detect-audio-language
- description: Detect the language of a text string with ApyHub, Azure, or Google. Route multilingual content into translation, classification, or indexing pipelines.
  name: AI Text Language Detection API
  slug: apyhub-ai-detect-language
- description: Summarize text or a web page URL with summary_length and output_language. Useful for article digests, research notes, and content previews.
  name: AI Summarize API
  slug: apyhub-ai-summarize-api
- description: 'Text Sentiment Analyzer lets you send a text string and get sentiment analysis back from one of three providers: ApyHub, Azure, or Google. Use it when you need to classify customer feedback, scan revi'
  name: AI Text Sentiment Analysis API
  slug: apyhub-analyze-text-sentiment
- description: Anonymize free-form text and return an azure or apyhub response object. Useful for redacting names and phone numbers before storage or sharing.
  name: AI Text Anonymization API
  slug: apyhub-anonymize-text
- description: Image Filter lets you apply a fixed set of transformations to an image and return the result as a file or a signed URL. Send either a binary image upload or an image url, choose a filter, and optional
  name: Image Filters API
  slug: apyhub-apply-filter
- description: Add a text or image watermark to each page of a PDF from an upload or URL. Get the result as a download or S3 URL.
  name: Apply Watermark on PDF API
  slug: apyhub-apply-watermark-on-pdf
- description: Add text or image watermarks to images from Base64, multipart upload, or URL. Returns binary output or a signed URL for branded assets and previews.
  name: Apply Watermark on Images API
  slug: apyhub-apply-watermark
- description: Ask natural-language questions about an uploaded PDF or a PDF URL. Returns an answer string for document search, review, and support workflows.
  name: Talk to PDF API
  slug: apyhub-ask-question-about-pdf
- description: Extract audio from a video URL or file into mp3, wav, aac, ogg, flac, wma, or ac3. Poll a job_id to get the output URL when it finishes.
  name: Audio Extractor from Video Job API
  slug: apyhub-audio-extract-from-video
- description: Ranks candidate strings against a source string and returns matches with Levenshtein distance. Useful for typo correction, deduplication, and closest-match lookup.
  name: Best Match Text Search API
  slug: apyhub-best-match-text-search
- description: Scan a webpage URL and get link statuses, redirect chains, response times, and a summary of broken links for audits and QA.
  name: Broken Link Checker API
  slug: apyhub-broken-link-checker-api
- description: Capture a public URL as a PDF download or signed link. Useful for archiving pages, sharing snapshots, and automating document workflows.
  name: Convert Webpage to PDF API
  slug: apyhub-capture-public-url-as-pdf
- description: Capture a webpage from a URL and get a PNG download or signed link. Useful for QA, visual regression, and archiving page states.
  name: Generate Webpage Screenshot API
  slug: apyhub-capture-webpage-screenshot
- description: Compose a subject image onto a new background using files or URLs. Returns PNG downloads or signed links for product shots and social assets.
  name: Change Background of Images API
  slug: apyhub-change-image-background
- description: Check whether an email belongs to an academic institution. Returns a boolean for education access, sign-up gating, and affiliation checks.
  name: Validate Academic Email API
  slug: apyhub-check-whether-an-email-belongs-to-an-aca
- description: Compare two text or code snippets and get ordered diff segments plus addition, deletion, and unchanged counts for review and change tracking.
  name: Differentiate Text API
  slug: apyhub-compare-text-or-code-snippets
- description: Compress JPEG, PNG, WebP, GIF, TIFF, and BMP images from a URL or upload. Get a smaller file or a signed download link.
  name: Compress Images API
  slug: apyhub-compress-images
- description: Compress videos from a file upload or URL and poll for a job URL. Returns job status, with a downloadable output when processing succeeds.
  name: Compress Video Job API
  slug: apyhub-compress-video-job
- description: Compress videos from an upload or URL and return a file or signed download link. Set compression percentage to shrink media for storage or delivery.
  name: Compress Video File API
  slug: apyhub-compress-video
- description: Classify text with a Google-backed response. Send text plus requested_service and get structured classification data for moderation and routing.
  name: AI Text Content Classification API
  slug: apyhub-content-classification
- description: Convert uploaded CSV files or CSV URLs into XLSX. Get either a streamed download or a signed link for spreadsheet workflows.
  name: Convert CSV to Excel API
  slug: apyhub-convert-csv-to-xlsx
- description: Convert uploaded CSV files, raw CSV text, or CSV URLs into XML files, inline XML, or signed S3 links. Useful for exports and integrations that expect XML.
  name: Convert CSV to XML API
  slug: apyhub-convert-csv-to-xml
- description: Get the exchange rate for a source and target currency pair on a given date. Useful for pricing, reporting, and historical FX checks.
  name: Convert Currency API
  slug: apyhub-convert-currency-pair-for-date
- description: Convert a source currency into multiple target currencies with optional date-based rates. Returns pair keys with rates or false when unavailable.
  name: Convert Currency to Multiple Currencies API
  slug: apyhub-convert-currency-to-multiple-currencies
- description: Convert HEIC and HEIF images to JPEG or PNG from a file upload or public URL. Get a binary download or a signed URL for the converted image.
  name: Convert HEIC to JPEG/PNG API
  slug: apyhub-convert-heic-heif-to-jpeg-or-png
- description: Convert an HTML content string into a PDF download or signed link. Useful for invoices, reports, and other HTML-based documents.
  name: Convert HTML Content to PDF API
  slug: apyhub-convert-html-content-to-pdf
- description: Convert a public HTML URL or uploaded .html/.htm file into DOCX. Return a downloadable file or an S3 URL for Word document workflows.
  name: Convert HTML to Word API
  slug: apyhub-convert-html-to-docx
- description: Convert HTML from a URL, base64 string, or file upload into PDF bytes or a signed link. Useful for invoices, reports, and printable web pages.
  name: Convert HTML to PDF API
  slug: apyhub-convert-html-to-pdf
- description: Convert uploaded images, base64 bytes, or image URLs into PDF binaries or signed links. Useful for scans, screenshots, and image-based document workflows.
  name: Convert Images to PDF API
  slug: apyhub-convert-image-to-pdf
- description: Convert JPEG images to AVIF from a public URL or multipart upload. Return either binary output or a signed download link.
  name: Convert JPEG to AVIF API
  slug: apyhub-convert-jpeg-to-avif-api
- description: JPEG to WebP Converter turns a JPEG or JPG image into a WebP file. Send either a public image URL or a binary image upload, and choose whether you want the result returned as a downloadable file or as
  name: Convert JPEG to WebP API
  slug: apyhub-convert-jpeg-to-webp
- description: Convert raw JSON, uploaded files, or JSON URLs into GraphQL SDL. Get inline text, a .graphql download, or a pre-signed S3 URL.
  name: Convert JSON to GraphQL Schema API
  slug: apyhub-convert-json-to-graphql-sdl
- description: Convert JSON objects, JSON URLs, or JSON files into Markdown. Get raw text, a .md download, or a pre-signed file link.
  name: Convert JSON to Markdown API
  slug: apyhub-convert-json-to-markdown
- description: Generate Mongoose schema code from JSON bodies, files, or URLs. Returns JS or TS output plus inference metadata for review.
  name: Convert JSON to Mongoose Schema API
  slug: apyhub-convert-json-to-mongoose-schema
- description: Convert JSON from a body, file, or URL into Prisma schema text or a .prisma file. Supports PostgreSQL, MySQL, SQLite, and MongoDB.
  name: Convert JSON to Prisma Schema API
  slug: apyhub-convert-json-to-prisma-schema
- description: Convert raw JSON, uploaded files, or JSON URLs into XML. Get a raw XML string, downloadable .xml file, or pre-signed S3 link.
  name: Convert JSON to XML API
  slug: apyhub-convert-json-to-xml
- description: Convert JSON files, raw JSON bodies, or JSON URLs into YAML. Get downloadable files, raw text, or pre-signed S3 URLs for downstream use.
  name: Convert JSON to YAML API
  slug: apyhub-convert-json-to-yaml
- description: Generate Zod schemas from JSON bodies, files, or URLs. Returns raw schema text, explain output, or downloadable files for typed validation.
  name: Convert JSON to Zod Schema API
  slug: apyhub-convert-json-to-zod-schema
- description: Convert Markdown files or Markdown URLs into HTML downloads or signed links. Useful for docs, changelogs, and static publishing workflows.
  name: Convert Markdown to HTML files API
  slug: apyhub-convert-markdown-to-html-files
- description: Convert Markdown from a JSON body or raw text/plain input into HTML. Use it for rendered content in docs, CMS, and publishing flows.
  name: Convert Markdown to HTML content API
  slug: apyhub-convert-markdown-to-html
- description: Convert raw Markdown, files, or URLs into JSON. Get inline output, a downloadable JSON file, or a signed S3 URL for document pipelines.
  name: Convert Markdown to JSON API
  slug: apyhub-convert-markdown-to-json
- description: Convert raw Markdown, uploaded files, or Markdown URLs into PDF. Get a downloadable file or a signed S3 URL back.
  name: Convert Markdown to PDF API
  slug: apyhub-convert-markdown-to-pdf
- description: Convert MP3 files or public MP3 URLs to AAC. Returns a binary file or a signed download URI for media workflows.
  name: Convert MP3 to AAC API
  slug: apyhub-convert-mp3-to-aac
- description: Convert PDF pages into JPG or PNG images from a file, URL, or base64 input. Returns a ZIP download or a download_url for the generated images.
  name: Convert PDF to Image API
  slug: apyhub-convert-pdf-pages-to-images
- description: Convert PDFs to editable DOCX from a file, URL, or base64 content. Returns a DOCX download or S3 download_url for document workflows.
  name: Convert PDF to Word API
  slug: apyhub-convert-pdf-to-docx
- description: Convert PDFs to PPTX from a file upload, public URL, or base64 input. Get a downloadable presentation file or a download_url.
  name: Convert PDF to PowerPoint API
  slug: apyhub-convert-pdf-to-powerpoint
- description: Convert a .pes embroidery file into a downloadable ZIP archive. Useful for packaging embroidery assets for transport or downstream file workflows.
  name: Convert PES to ZIP API
  slug: apyhub-convert-pes-to-zip
- description: Convert PNG images to WebP from an upload or a URL. Get a binary file or a signed result link for web delivery and asset pipelines.
  name: Convert PNG to WebP API
  slug: apyhub-convert-png-to-webp
- description: Convert .ppt, .pptx, or .odp files to PDF from uploads, base64, or URLs. Get a binary PDF or a signed link for review and sharing.
  name: Convert Presentations to PDF API
  slug: apyhub-convert-presentation-to-pdf
- description: Parse RSS or Atom feeds from a file or URL into JSON. Useful for ingesting blog, news, or podcast feeds into apps and pipelines.
  name: Convert RSS to JSON API
  slug: apyhub-convert-rss-to-json
- description: Convert spreadsheet uploads, URLs, or base64 bytes to PDF. Get binary downloads or signed links for Excel, XLSX, and ODS files.
  name: Convert Spreadsheets to PDF API
  slug: apyhub-convert-spreadsheet-to-pdf
- description: Convert SVG files or URLs to WebP. Get binary downloads or signed URLs for image pipelines, CMS imports, and asset standardization.
  name: Convert SVG to WebP API
  slug: apyhub-convert-svg-to-webp
- description: Convert text, file uploads, or document URLs into MP3 audio. Get a binary download or a signed link with male or female voice selection.
  name: Convert Text to Speech API
  slug: apyhub-convert-text-to-speech
- description: Convert uploaded videos or video URLs into mp4, mkv, avi, mov, flv, 3gp, or webm. Track jobs with a job ID and status response.
  name: Convert Video Formats Job API
  slug: apyhub-convert-video-formats-job
- description: Convert video files from a URL or upload into mp4, mkv, avi, mov, flv, 3gp, or webm. Get a download file or a signed cloud link.
  name: Convert Video Formats API
  slug: apyhub-convert-video-formats
- description: Convert WAV files to MP3 from uploads or public URLs. Get a streamed binary download or a signed link for the converted audio.
  name: Convert WAV to MP3 API
  slug: apyhub-convert-wav-to-mp3
- description: Convert Word files, base64 documents, or remote URLs to PDF. Get a binary download or a signed link for `.doc`, `.docx`, `.odt`, and `.rtf` inputs.
  name: Convert Word to PDF API
  slug: apyhub-convert-word-to-pdf
- description: Convert XML from a raw body, file upload, or URL into CSV text, a downloadable file, or a signed URL. Useful for feeds and ETL pipelines.
  name: Convert XML to CSV API
  slug: apyhub-convert-xml-to-csv
- description: Convert raw XML, XML files, or XML URLs into JSON. Get inline data, a downloadable JSON file, or a pre-signed S3 URL for automation and ETL.
  name: Convert XML to JSON API
  slug: apyhub-convert-xml-to-json
- description: Convert raw YAML, uploaded files, or YAML at a URL into inline JSON, a downloadable file, or a signed S3 URL.
  name: Convert YAML to JSON API
  slug: apyhub-convert-yaml-to-json
- description: Count working days between two dates for a country. Returns total days, weekends, holidays, and working_days for scheduling and payroll logic.
  name: Working Day Calculator API
  slug: apyhub-count-working-days
- description: Create encrypted ZIP archives from uploaded files or remote URLs. Stream the ZIP or return a signed download link for controlled sharing.
  name: Generate Secure Archives API
  slug: apyhub-create-password-protected-zip
- description: Bundle uploaded files or remote URLs into a ZIP. Get a streamed ZIP download or a signed link, with optional output file naming.
  name: Generate Archives API
  slug: apyhub-create-zip
- description: Crop raster images by URL or file upload and get a binary file or signed download link. Use box crops or margin insets for thumbnails and asset prep.
  name: Crop Images API
  slug: apyhub-crop-image
- description: Convert raw CSV, uploaded files, or CSV URLs into JSON arrays, downloadable files, or pre-signed S3 links for import and ETL workflows.
  name: Convert CSV to JSON API
  slug: apyhub-csv-to-json
- description: Lookup a country by ISO 3166-1 alpha-2 code and get its name, alpha-3 code, currency, calling codes, and subdivisions.
  name: Country Information API
  slug: apyhub-detailed-info-for-a-single-country
- description: Detect common objects from an uploaded image or image URL. Returns provider-specific results for Azure, Google, or ApyHub vision detectors.
  name: AI Image Objects Detection API
  slug: apyhub-detect-common-visual-objects
- description: Scan image files or URLs for explicit or sensitive content. Returns provider-specific results from ApyHub, Azure, or Google for moderation workflows.
  name: AI Image Explicit Content Detection API
  slug: apyhub-detect-explicit-or-sensitive-content
- description: Face Detection identifies human faces in an image you send as a file or by URL. Use it when you need to flag portrait photos, pre-check user uploads, or build image workflows that depend on knowing wh
  name: AI Image Face Detection API
  slug: apyhub-detect-human-faces
- description: Identify landmarks from image uploads or image URLs. Returns detector responses from ApyHub, Azure, or Google for vision workflows.
  name: AI Image Landmark Detection API
  slug: apyhub-detect-landmarks
- description: Detect the spoken language in a video file or video URL. Returns Azure language code and confidence for routing transcription and review.
  name: AI Video Language Detection API
  slug: apyhub-detect-language-video
- description: Detect the language of a text sample and get the language name, ISO codes, script, and confidence score for routing or localization.
  name: Language Detection API
  slug: apyhub-detect-language
- description: Detect logos and brand marks from an image file or URL. Returns provider-specific results from Azure, Google, or ApyHub vision models.
  name: AI Image Brand/Logo Detection API
  slug: apyhub-detect-logos-and-brands
- description: Detect people in media from a file or URL using Azure or Google. Returns provider-specific results in a structured data object.
  name: AI Video Person Detection API
  slug: apyhub-detect-persons
- description: Analyze a video file or URL and get shot change results back under Azure or Google. Useful for scene segmentation, indexing, and review workflows.
  name: AI Video Shot Change Detection API
  slug: apyhub-detect-shot-changes
- description: Detect brands from a video URL or uploaded file. Returns provider-scoped output for Azure or Google based on the service you request.
  name: AI Video Brand/Logo Detection API
  slug: apyhub-detect-video-brands
- description: Analyze a video from a file or URL with Azure or Google. Returns provider-specific label results for search, moderation, and media workflows.
  name: AI Video Label Detection API
  slug: apyhub-detect-video-labels
- description: Detect objects from a video file or URL using Azure or Google routes. Returns provider-specific results under data for media review and indexing.
  name: AI Video Object Detection API
  slug: apyhub-detect-video-objects
- description: Extract text from video URLs or uploads using Azure or Google. Returns provider-specific results for OCR workflows, indexing, and review.
  name: AI Video Text Detection API
  slug: apyhub-detect-video-text
- description: Send a file or document URL and get extracted results in a structured response. Route through Azure or ApyHub for document parsing workflows.
  name: AI Document Data Extraction API
  slug: apyhub-document-extraction
- description: Check whether a domain is available, taken, or indeterminate. Validate candidate names for signup flows, registrars, and domain search tools.
  name: Domain Availability API
  slug: apyhub-domain-availability-api
- description: Analyze sentiment around entities mentioned in text. Send text with requested_service=google and receive a data.google result for NLP workflows.
  name: AI Text Entity Sentiment Analysis API
  slug: apyhub-entity-sentiment-analysis
- description: Detect explicit material in video files or URLs using Azure or Google routes. Returns provider-specific results for content moderation workflows.
  name: AI Video Explicit Content Detection API
  slug: apyhub-explicit-content-detection
- description: Analyze public article URLs and return ranked keyword groups with scores. Useful for content clustering, topic analysis, and SEO workflows.
  name: Analyse Keywords API
  slug: apyhub-extract-and-group-keywords-from-article
- description: Extract audio from a video upload or URL as binary output or a signed download link. Choose segment length, start time, and audio format.
  name: Audio Extractor from Video API
  slug: apyhub-extract-audio-from-video
- description: ID Data Extraction lets you send an ID document as a file or by URL and get extracted identity data back. Choose the requestedservice value to route the request to apyhub or azure, and, for Azure-back
  name: AI Document ID Extraction API
  slug: apyhub-extract-id-data
- description: Extract ExifTool metadata from an uploaded image or image URL. Get format, size, dimensions, MIME type, and other file details in JSON.
  name: Extract Image Metadata API
  slug: apyhub-extract-image-metadata
- description: Extract structured invoice data from a file or URL. Returns ApyHub or Azure invoice parsing output for accounts payable and ingestion workflows.
  name: AI Document Invoice Data Extraction API
  slug: apyhub-extract-invoice-data
- description: Extract keywords from plain text for tagging, search, and content analysis. Supports ApyHub or Azure results with optional language selection.
  name: AI Text Keyword Extraction API
  slug: apyhub-extract-keywords-from-text
- description: Extract absolute URLs from a webpage, with optional headers and URL safety checks. Useful for crawling, audits, and sitemap collection.
  name: Extract Links from Webpage API
  slug: apyhub-extract-links-from-webpage
- description: Decrypt uploaded or remote .zip, .rar, or .7z archives with a password. Returns signed URLs for each extracted file.
  name: Unarchive Secured Files API
  slug: apyhub-extract-password-protected-archive
- description: Extract reading data from a file upload or URL. Returns ApyHub or Azure parsing output for document workflows and indexing.
  name: OCR Document Data Extraction API
  slug: apyhub-extract-read-data
- description: Extract receipt data from uploads or URLs. Returns ApyHub or raw Azure parsing output for expense tracking and receipt processing.
  name: AI Document Receipt Data Extraction API
  slug: apyhub-extract-receipt-data
- description: Extract URLs from a website’s sitemaps, with optional sitemap metadata and async job polling. Useful for SEO audits, crawl seeds, and site inventory.
  name: Extract Sitemap from URL API
  slug: apyhub-extract-sitemap-from-url-api
- description: Extract table data from a file or URL. Returns Azure or ApyHub parsing output for invoice, report, and document table capture.
  name: AI Document Table Data Extraction API
  slug: apyhub-extract-table-data
- description: Extract text from image files or image URLs. Returns structured OCR output via Azure Vision Read API or ApyHub OCR for parsing and indexing.
  name: AI Image Optical Character Recognition (OCR) API
  slug: apyhub-extract-text-from-image
- description: Extract text from a PDF by URL or file upload. Supports page ranges and region bounds, returning plain text in a single data field.
  name: Extract Text from PDF API
  slug: apyhub-extract-text-from-pdf
- description: Extract plain text from .doc or .docx files by URL or upload. Returns a single text field for indexing, search, and document workflows.
  name: Extract Text from Word API
  slug: apyhub-extract-text-from-word
- description: Read metadata from a video file or URL and get nested audio, video, and file details in JSON for validation, indexing, or processing.
  name: Extract Video Metadata API
  slug: apyhub-extract-video-metadata
- description: Extract visible text from a webpage as a string or line array. Useful for crawling, search indexing, and SEO checks.
  name: Extract Text from Webpage API
  slug: apyhub-extract-visible-text-from-awebpage
- description: Detect faces from uploaded files or remote URLs using Azure or Google. Returns provider-specific results in a data object for media workflows.
  name: AI Video Face Detection API
  slug: apyhub-face-detection
- description: Compare a source string against a space-separated target and get matching words back. Useful for autocomplete, filtering, and text normalization.
  name: Fuzzy Text Search API
  slug: apyhub-fuzzy-search
- description: Bar Chart Generator creates bar chart images and shareable chart links from a title and a list of bar values. Send a title, data array, and optional theme or options; get back either a binary image fr
  name: Generate Bar Graph API
  slug: apyhub-generate-bar-graph
- description: Generate Code128 barcodes from a text string and download them or get a pre-signed cloud URL. Useful for labels, inventory, and ticketing.
  name: Generate Barcode API
  slug: apyhub-generate-barcode
- description: Convert a video URL or file into a GIF job and poll for a download URL. Adjust size, speed, duration, and start time for the clip you need.
  name: Generate GIF from Video Job API
  slug: apyhub-generate-gif-from-video
- description: Convert uploaded videos or remote video URLs into GIFs. Control size, speed, start time, and duration, with binary download or signed link output.
  name: Generate GIF from Video API
  slug: apyhub-generate-gif
- description: Generate downloadable .ics files or signed links from event details, with reminders, recurrence, all-day events, and time zone support.
  name: Generate iCal API
  slug: apyhub-generate-ical-event
- description: 'Link Preview fetches a URL and returns the metadata you need to build a rich preview card. Send a URL, and Link Preview returns the page title, description, images, videos, favicons, site name, media '
  name: Generate Link Preview API
  slug: apyhub-generate-link-preview
- description: Generate Open Graph PNGs from JSON with title, subtitle, description, and brand colors. Use a file or signed URL in social preview workflows.
  name: Basic OG Image Generator API
  slug: apyhub-generate-og-image
- description: Generate pie chart images from labeled values, optional colors, and chart styling. Returns a pre-signed URL or binary image for dashboards and reports.
  name: Generate Pie Chart API
  slug: apyhub-generate-pie-chart
- description: Generate PNG previews from uploaded files or remote URLs. Stream the image or return a signed link, with optional width control.
  name: Generate File Preview API
  slug: apyhub-generate-png-preview
- description: Create QR codes from text, vCards, or Wi‑Fi details. Download the image or get a pre-signed cloud URL, with logo, color, and error-correction options.
  name: Generate QR Code API
  slug: apyhub-generate-qr-code
- description: Generate calendar heatmap charts from dated numeric data. Returns a chart image file or a pre-signed image URL for dashboards and reports.
  name: Generate HeatMap Chart API
  slug: apyhub-generate-simple-heatmap-chart
- description: Generate radar chart images or pre-signed links from titles, labels, and series data. Useful for score comparisons, dashboards, and reports.
  name: Generate Radar Chart API
  slug: apyhub-generate-simple-radar-chart
- description: Create stacked bar chart images from titled data arrays with optional colors and layout settings. Get a pre-signed URL or binary image for reporting and dashboards.
  name: Generate Stacked Graph API
  slug: apyhub-generate-stacked-bar-chart
- description: Generate SVG badges from a label and message, with optional colors. Download the SVG or get a signed URL for READMEs, docs, and CI status.
  name: Generate SVG Badge API
  slug: apyhub-generate-svg-badge
- description: Extract a PNG frame from a video file or URL at a chosen timestamp, with binary download or signed link output for previews and galleries.
  name: Generate Thumbnail from Video API
  slug: apyhub-generate-thumbnail-from-video
- description: Create thumbnails from an uploaded image or image URL. Set width and height, and get binary output or a signed URL back.
  name: Generate Image Thumbnails API
  slug: apyhub-generate-thumbnail
- description: Create a thumbnail from a video file or URL, choose the frame time and output size, and poll for a result URL.
  name: Generate Thumbnail from Video Job API
  slug: apyhub-generate-video-thumbnail-job-api
- description: Clip a video file or video URL into a short output. Set start time, duration, and optional size, then poll for a job_id and output URL.
  name: Generate Video Thumbnail Job API
  slug: apyhub-generate-video-thumbnail-job
- description: Trim a short clip from an uploaded video or a remote video URL. Get binary output or a signed link for previews, samples, and media workflows.
  name: Generate Video Thumbnail API
  slug: apyhub-generate-video-thumbnail
- description: Add text or image watermarks to videos from a URL or file. Poll a job ID for the finished video URL when processing completes.
  name: Generate Watermark For Videos Job API
  slug: apyhub-generate-video-watermark
- description: Add text or image watermarks to uploaded videos or remote video URLs. Returns a processed video download or a signed link for the result.
  name: Generate Watermark For Videos API
  slug: apyhub-generate-watermark-for-videos
- description: Convert JSON objects, arrays, files, or URLs into CSV. Get inline text, a downloadable file, or a pre-signed S3 URL for exports.
  name: Convert JSON to CSV API
  slug: apyhub-json-to-csv
- description: Get a structured list of countries with ISO codes, currency details, emojis, and calling codes for forms, routing, and localization.
  name: Countries Dictionary API
  slug: apyhub-list-all-countries
- description: Currency Directory gives you a complete list of currencies with their ISO 4217 code, English name, emoji, and symbol. Send a GET request and receive a data array of currency objects. Each item include
  name: Currencies Dictionary API
  slug: apyhub-list-all-currencies
- description: Get a live list of time zones with country codes, IANA names, current UTC offsets, and abbreviations for scheduling and locale-aware apps.
  name: Timezones Dictionary API
  slug: apyhub-list-timezones
- description: Verify a VAT number and retrieve the matching company name, address, country code, and validity status for onboarding and invoicing checks.
  name: VAT Company Lookup API
  slug: apyhub-lookup-vat-company
- description: Merge uploaded files or public file URLs into a single PDF. Returns a PDF download or an S3 URL for documents, images, spreadsheets, and more.
  name: Merge Files to PDF API
  slug: apyhub-merge-files-to-pdf
- description: Batch resolve domains or IPs for A, AAAA, MX, NS, TXT, CNAME, and PTR records. Get per-row status plus record data for each query.
  name: DNS Batch Lookup API
  slug: apyhub-mono-go-dns-batch-lookup
- description: Get ISO 639-1 languages with code, English name, and native name. Useful for language pickers, localisation, and code-to-name lookups.
  name: Language Dictionary API
  slug: apyhub-mono-go-language-list
- description: Get public holidays by country and year, plus the supported country list. Use it for business-day logic, scheduling, and holiday calendars.
  name: Public Holidays API
  slug: apyhub-mono-go-public-holidays
- description: Generate donut chart images from a title and labeled data. Get a binary image or a pre-signed URL for dashboards, reports, and status breakdowns.
  name: Generate Donut Graph API
  slug: apyhub-mono-go-simple-donut-chart-generation
- description: Convert SVGs from a URL or multipart upload into PNG. Get binary output or a signed download URL for previews and image delivery.
  name: Convert SVG to PNG API
  slug: apyhub-mono-go-svg-to-png-conversion
- description: Convert WebP images to AVIF from a public URL or multipart upload. Get either binary file downloads or a signed URL for the converted image.
  name: Convert WebP to AVIF API
  slug: apyhub-mono-go-webp-to-avif-conversion
- description: Convert WebP images to JPEG from a URL or multipart upload. Get a binary file or a signed download URL for downstream use.
  name: Convert WebP to JPEG API
  slug: apyhub-mono-go-webp-to-jpeg-conversion
- description: Convert WebP images to PNG from file uploads or image URLs. Download the PNG directly or get a signed URL for the converted file.
  name: Convert WebP to PNG API
  slug: apyhub-mono-go-webp-to-png-conversion
- description: Convert MP3 files or public audio URLs to WAV. Get the result as a binary download or a signed URL for audio workflows and processing.
  name: Convert MP3 to WAV API
  slug: apyhub-mp3-to-wav-conversion
- description: Parse a raw User-Agent string into browser, platform, device, and engine data. Useful for analytics, request logging, and bot detection.
  name: Extract User Agent API
  slug: apyhub-parse-user-agent-string
- description: Compare a source word against candidate strings using Metaphone or Soundex. Returns matching words with shared phonetic codes for deduping and search.
  name: Phonetic Text Search API
  slug: apyhub-phonetic-match
- description: Pixelize faces from uploaded images or image URLs. Returns a processed URL or a no-faces message for privacy-safe redaction.
  name: Pixelize Face API
  slug: apyhub-pixelize
- description: Rank fuzzy matches for a search term against space-separated text. Returns matches with Levenshtein distance for lookup and typo-tolerant search.
  name: Ranked Text Search API
  slug: apyhub-ranked-text-search
- description: Extract names, organizations, and places from text using Azure, Google, or ApyHub. Useful for enrichment, indexing, and document analysis.
  name: AI Text Entity Recognition API
  slug: apyhub-recognize-entities-in-text
- description: Background Remover removes the background from an image and returns either a PNG download or a signed file URL. Send a raster image directly as multipart form data, or provide an imageurl to fetch the
  name: Remove Background from Images API
  slug: apyhub-remove-background-from-images
- description: Remove metadata from uploaded images or image URLs. Return a cleaned binary file or a signed URI, with optional EXIF key and GPS cleanup.
  name: Remove Image Metadata API
  slug: apyhub-remove-image-metadata
- description: Resize uploaded images or images from a URL to exact width and height. Get a binary file or a signed download link, with optional format preservation.
  name: Resize Images API
  slug: apyhub-resize-image
- description: Analyze plain text with readability metrics, word and sentence stats, and English or German scoring. Useful for checking copy before publication.
  name: Readability Scores API
  slug: apyhub-score-readability-of-plain-text
- description: Analyze documents or web pages for readability scores, text stats, and grade-level classification. Useful for content review and plain-language checks.
  name: Readability Scores Documents API
  slug: apyhub-score-readability
- description: Get ranked search results for a keyword with language and location options. Returns URLs, titles, domains, and descriptions for SEO analysis.
  name: SERP Rank Checker API
  slug: apyhub-serp-rankings-for-keyword
- description: Convert uploaded files or media URLs to text using Azure or Google transcription. Get a provider-specific response for speech search, review, and analytics.
  name: AI Video Transcriber API
  slug: apyhub-speech-transcription
- description: Add headers and footers to PDFs from a URL or file upload. Return a stamped PDF as a binary file or signed URL, with text or PNG image support.
  name: Apply Watermark and Footers on PDF API
  slug: apyhub-stamp-header-footer-on-pdf
- description: Summarize PDF, DOCX, DOC, or ODT files from an upload or URL. Returns a plain-text summary with short, medium, or long length options.
  name: AI Summarize Documents API
  slug: apyhub-summarize-documents
- description: Analyze text with a Google-backed syntax service. Send text, encoding, and requested_service; get a structured data.google result back.
  name: AI Text Syntax Analysis API
  slug: apyhub-syntax-analysis
- description: Compare two strings with Levenshtein distance. Send source and target, get an integer edit distance for fuzzy matching and typo checks.
  name: Text Distance Search API
  slug: apyhub-text-distance-search
- description: Check text with Google moderation using a text string and requested_service. Returns a google result inside data for content screening workflows.
  name: AI Text Moderation API
  slug: apyhub-text-moderation
- description: Compare a source string and a target string and get a 0 to 1 similarity score. Useful for fuzzy matching, duplicate checks, and text ranking.
  name: Text Similarity Search API
  slug: apyhub-text-similarity-search
- description: Transcribe WAV files or WAV URLs with an Azure locale. Returns plain text in `data` for indexing, search, and voice-note workflows.
  name: Convert Speech to Text API
  slug: apyhub-transcribe-speech-to-text
- description: Translate uploaded documents or document URLs into a target language. Returns translated text, translated language, and optional detected language.
  name: Translate Documents API
  slug: apyhub-translate-documents
- description: Send a ZIP, RAR, or 7Z file or URL and get signed URLs for each extracted file. Useful for upload pipelines and document workflows.
  name: Unarchive Files API
  slug: apyhub-unarchive-files
- description: Validate a 12-digit Aadhaar number from a request body string and get a boolean result. Useful for KYC and identity form checks.
  name: Validate Aadhaar API
  slug: apyhub-validate-aadhaar-number
- description: Validate uploaded files or file URLs against their extension and MIME type. Get the detected type, validity flag, and a clear mismatch message.
  name: Validate File Type API
  slug: apyhub-validate-file-type
- description: Validate an IBAN from a request body and get back validity plus parsed fields like country code, BBAN, and printable format.
  name: Validate IBAN API
  slug: apyhub-validate-iban
- description: Validate an IFSC code and get bank details like branch, city, state, and phone. Returns false when the code is not found or deleted.
  name: Validate IFSC API
  slug: apyhub-validate-ifsc-bank-code
- description: Validate India Postcode Validator checks whether a postcode exists in its lookup table. Send a postcode string in the request body; spaces are ignored for matching. The response is intentionally simpl
  name: Validate Indian Postcodes API
  slug: apyhub-validate-indian-postcode
- description: Validate BIC/SWIFT codes and extract bank, branch, country, and location codes. Useful for payment forms and banking data checks.
  name: Validate SWIFT/BIC API
  slug: apyhub-validate-swift-bic-code
- description: Validate a UK postcode from a request body and get a boolean result. Useful for screening address data before storage, routing, or checkout.
  name: Validate UK Postcodes API
  slug: apyhub-validate-uk-postcode
- description: Validate up to 10 VAT numbers per request and get per-item valid results, with lookup errors flagged separately for tax and billing workflows.
  name: Validate EU VAT Batch API
  slug: apyhub-validate-vat-batch
- description: Validate a VAT number from the request body and get a boolean result in data. Useful for checking customer or supplier tax IDs before billing or storage.
  name: Validate EU VAT API
  slug: apyhub-validate-vat-number
- description: Check whether an email address is valid and deliverable. Screen signups and lead lists with an optional disposable-domain check.
  name: Validate Email DNS API (Including Disposable Emails)
  slug: apyhub-verify-email-validity-and-deliverability
- description: Extract title, links, images, tables, headings, sections, and page metadata from a webpage URL. Useful for crawlers, content pipelines, and search indexing.
  name: AI-ready Clean Data Extractor API
  slug: apyhub-webpage-extractor-api
- description: Temporary Email gives you disposable email addresses you can create, read from, and delete through a simple API. Use it when you need a short-lived inbox for signups, verification flows, QA, or any wo
  name: Temporary and Disposable Emails API
  slug: boomlify-temporary-and-disposable-emails-api
- description: Audit a webpage URL for rich result eligibility. Returns checked types, eligibility status, and missing or recommended fields for each result type.
  name: Check Rich Results API
  slug: chisleroff-check-rich-results
- description: Convert a webpage URL into Markdown, with title, character count, and readability_success. Useful for content ingestion, archiving, and docs workflows.
  name: Convert HTML to Markdown API
  slug: chisleroff-convert-html-to-markdown
- description: Detect the technologies used by a webpage from its URL. Returns the source URL and a list of detected technologies for audits and enrichment.
  name: Detect Tech Stack API
  slug: chisleroff-detect-tech-stack
- description: Generate Open Graph images from title and styling fields. Returns a binary image for blog posts, product pages, and social sharing cards.
  name: Dynamic OG Image API
  slug: chisleroff-dynamic-og-image-generation
- description: Audit a webpage URL and get a score, grade, structured-data breakdown, and top fixes. Useful for checking metadata and rich-result readiness.
  name: Evaluate SEO Health API
  slug: chisleroff-evaluate-seo-health
- description: Extract article text from a webpage URL and get title, author, date, images, language, word count, source URL, and confidence scores.
  name: Extract Article From Web API
  slug: chisleroff-extract-article
- description: Extract emails, phones, addresses, and social links from a webpage URL. Useful for lead enrichment, site audits, and contact validation.
  name: Extract Contact Information API
  slug: chisleroff-extract-contact-information
- description: Extract sku, name, brand, price, images, rating, and more from a product page URL. Useful for catalog enrichment, feed building, and price tracking.
  name: Extract Product Information API
  slug: chisleroff-extract-product-information
- description: Checks a webpage URL and returns metadata, tech stack, performance, broken links, security headers, and mobile-friendliness for SEO and QA.
  name: Full Site Audit API
  slug: chisleroff-full-site-audit
- description: Convert raw HTML into a PDF file with page size, margins, orientation, and background control. Useful for invoices, reports, and document exports.
  name: Convert and Format raw HTML to PDF API
  slug: chisleroff-pdf-from-html
- description: Convert an http or https page URL into a PDF binary. Use layout options like page size, margins, headers, footers, and background printing.
  name: Advanced Webpage to PDF API
  slug: chisleroff-pdf-from-url
- description: Audit a webpage URL for CSP, HSTS, X-Content-Type-Options, Referrer-Policy, and X-Frame-Options. Get a score and header flags for quick security checks.
  name: Security Headers Audit API
  slug: chisleroff-security-headers-audit
- description: Validate raw HTML for JSON-LD, microdata, meta tags, Open Graph, and Twitter cards. Get a summary of warnings, errors, and rich result eligibility.
  name: Validate HTML API
  slug: chisleroff-validate-html
- description: Validate structured data on a URL and retrieve JSON-LD, microdata, meta tags, Open Graph, Twitter cards, and a validation summary.
  name: Validate Schema API
  slug: chisleroff-validate-schema
- description: Analyze text for counts, readability, top keywords, and reading time. Useful for content review, SEO checks, and simple language statistics.
  name: Basic Text Analysis API
  slug: creightonnick0-analyze-text
- description: Calculate business-day adds, counts, checks, and holiday lists with country calendars for US, GB, CA, AU, DE, FR, and IN.
  name: Business Days Calculator API.
  slug: creightonnick0-business-day-math
- description: Compare foreground and background colors and get WCAG 2.1 contrast ratio, AA/AAA pass-fail, luminance, and a recommendation.
  name: Check WCAG Color Contrast API
  slug: creightonnick0-color-contrast-checker
- description: Convert a color string in hex, RGB, or HSL and get structured JSON back for palette, accessibility, and format handling in apps.
  name: Convert Color Formats API
  slug: creightonnick0-color-converter
- description: Convert text into slug, camelCase, snake_case, and other common cases. Useful for URLs, identifiers, headings, and text normalisation.
  name: Convert Case & Slug from Text API
  slug: creightonnick0-convert-case-and-slug
- description: Convert ISO strings, unix epochs, or now into UTC, localized, and relative formats. Returns weekday, week number, and epoch values.
  name: Convert Date & Time Formats API
  slug: creightonnick0-convert-date-time
- description: Convert integer strings between bases 2 to 36, with auto-detection for 0x, 0o, and 0b prefixes. Useful for radix formatting and mixed-base inputs.
  name: Convert Number Bases API
  slug: creightonnick0-convert-number-bases
- description: Compute upcoming fire times for a 5-field cron expression. Return next_runs, count, timezone, and the reference time in UTC.
  name: Advanced Schedule Cron API
  slug: creightonnick0-cron-next-run-calculator
- description: Decode a JWT from a token string and inspect its header, payload, and claims without verification. Useful for debugging auth flows and token contents.
  name: JWT Decoder API
  slug: creightonnick0-decode-jwt
- description: Generate batches of UUIDs, ULIDs, NanoIDs, hex strings, or short tokens. Useful for test data, fixtures, and temporary IDs.
  name: Generate IDs In Batch API
  slug: creightonnick0-generate-id-batch
- description: Get a year-level calendar for phases, sign ingresses, sabbats, and planetary events from a single year input.
  name: Get Lunar Calendar API
  slug: creightonnick0-get-calendar-year
- description: Get Natal Moon phase, zodiac sign, and illumination for a birth date and time. Useful for astrology apps and birth-chart lookups.
  name: Get Natal Moon API
  slug: creightonnick0-get-natal-moon
- description: Get New, First Quarter, Full, and Last Quarter moon dates for a range in UTC, with optional local time zone output for calendar apps.
  name: Get Moon Phases & Void-of-Course Windows
  slug: creightonnick0-get-phases
- description: Get 24 planetary hours for a latitude, longitude, and date, with sunrise and sunset. Useful for astrology and solar-time scheduling.
  name: Get Planetary Hours API
  slug: creightonnick0-get-planetary-hours
- description: Get Wheel of the Year sabbats and solstices/equinoxes for the Northern or Southern hemisphere. Useful for calendars and seasonal reference data.
  name: Get Sabbat Dates API
  slug: creightonnick0-get-sabbats
- description: Map filenames or extensions to MIME types, or reverse a MIME type back to a filename-style value. Useful for uploads, headers, and file validation.
  name: MIME Type Lookup from File Name API
  slug: creightonnick0-mime-type-lookup
- description: Score a password with strength, entropy, warnings, and crack-time analysis, or generate a strong password of a chosen length.
  name: Generate/Score Password API
  slug: creightonnick0-password-strength-evaluation
- description: Convert local datetimes across IANA time zones with DST-aware offsets, or plan meetings across multiple zones. Returns structured source, UTC, and target times.
  name: Convert Timezone and Meeting Planner API
  slug: creightonnick0-timezone-conversion
- description: Validate or generate barcode check digits for EAN, UPC, and ISBN values. Returns validity and check-digit fields for product data checks.
  name: Validate Or Generate Barcode Check Digits API
  slug: creightonnick0-validate-barcode-check-digits
- description: Validate card numbers with Luhn and length checks, identify the network, and return masked or formatted values for safe handling.
  name: Validate Payment Card API
  slug: creightonnick0-validate-card-number
- description: Validate phone numbers in E.164 or national format and get normalized country-aware output. Useful for signup forms, contact cleanup, and SMS workflows.
  name: Validate and Format Phone Number API
  slug: creightonnick0-validate-phone-number
- description: Classify text as positive or negative with a confidence score. Process single messages or batches for feedback triage and content moderation.
  name: Analyze Multiple Text Sentiment API
  slug: dosvak-analyze-sentiment
- description: Apply warm, cool, vivid, mono, or dream filters to an uploaded image and receive the edited file back. Tune effect intensity for photo styling or batch edits.
  name: Apply Face Filters API
  slug: dosvak-apply-face-filters
- description: Upload a binary image and get back a stylized version in painting, watercolor, sketch, or oil mode. Adjust strength from 0 to 1.
  name: Apply Style Filters on Image API
  slug: dosvak-apply-image-style-transfer
- description: Enhance an uploaded image with CLAHE contrast adjustment and saturation boosting. Returns the processed image as binary output.
  name: Enhance Image API
  slug: dosvak-auto-enhance-image
- description: Detect and segment objects in JPEG, PNG, or WebP images. Returns mask data, bounding boxes, image size, and quality scores for each segment.
  name: Image Segmentation API
  slug: dosvak-auto-segmentation
- description: Remove image backgrounds with SAM-2 auto-segmentation. Send an image file up to 20 MB and get a transparent PNG back for editing or publishing.
  name: Remove Background from Image File API
  slug: dosvak-background-removal
- description: Render Code128, EAN-13, EAN-8, ISBN-13, or UPC-A barcodes from a data string. Get a PNG for labels, inventory, and product workflows.
  name: Generate Simple Barcode API
  slug: dosvak-barcode
- description: Encode UTF-8 text to Base64 or decode Base64 back to text. Useful for transport, inspection, and round-trip checks in scripts and integrations.
  name: Encode and Decode Base64 API
  slug: dosvak-base64-encode-decode
- description: Language Detection identifies the language of text you send in q and returns the detected language with a confidence score. It works with a single string or an array of strings, so you can classify on
  name: Basic Language Detection API
  slug: dosvak-basic-detect-language
- description: Batch summarize up to 10 texts with BART or Pegasus. Returns each summary with input and summary lengths for review or downstream AI workflows.
  name: Batch Text Summarization API
  slug: dosvak-batch-summarize-text
- description: Detect faces in an image and return a blurred, pixelated, or blacked-out version. Useful for anonymising photos before publishing or sharing.
  name: Blur/Pixelate or Black out Image Faces API
  slug: dosvak-blur-faces
- description: Analyze a domain or URL and get a structured site profile with classification and keywords. Useful for enrichment, SEO research, and lead scoring.
  name: Extract Domain Insights API
  slug: dosvak-build-domain-profile
- description: Convert an uploaded image into a cartoon-style PNG. Control style, detail, smoothing, and edge strength for avatars, graphics, and image effects.
  name: Convert Image to Cartoon API
  slug: dosvak-cartoonize-image
- description: Count place categories inside a bounding box using min/max lat and lon. Useful for map filtering, location analytics, and area summaries.
  name: US places Category Breakdown API
  slug: dosvak-category-breakdown-in-bbox
- description: Fetch category facet data with optional limit, page language, and country code filters. Useful for localized catalog navigation and market-specific browse pages.
  name: List  Website Category API
  slug: dosvak-category-facets
- description: Send messages and receive a model-generated reply with usage, timestamps, and choices. Useful for chat apps, assistants, and task-oriented workflows.
  name: Chat Completion Generation API
  slug: dosvak-chat-completions
- description: Check whether an email domain has MX records. Returns email, domain, has_mx, and mx_records for deliverability checks and list hygiene.
  name: Email MX Lookup API
  slug: dosvak-check-email-mx
- description: Predict Tier 1 IAB categories from a URL, text, title, domain, or keywords. Returns ranked labels with scores for content classification and ad targeting.
  name: IAB Tier 1 Content Classification API
  slug: dosvak-classify-iab-tier-1
- description: Classify URLs, titles, text, domains, or keywords into IAB Tier 2 labels. Returns ranked predictions with scores for ad taxonomy and content routing.
  name: IAB Tier 2 Content Classification API
  slug: dosvak-classify-iab-tier-2
- description: Classify a URL, text, title, domain, or keywords into IAB Tier 3 labels. Returns a tier and ranked predictions with scores for content tagging.
  name: IAB Tier 3 Content Classification API
  slug: dosvak-classify-iab-tier-3
- description: Classify an uploaded image as safe or NSFW and get a confidence score plus per-class scores. Useful for moderation and upload screening.
  name: Classify NSFW Image API
  slug: dosvak-classify-nsfw-image
- description: Predict labels from URL, text, title, domain, or keywords. Get scored results per tier for content tagging, routing, and taxonomy assignment.
  name: IAB Unified Content Classification API
  slug: dosvak-classify-unified
- description: Convert a HEX color into RGB and HSL values. Useful for design tools, theming, and frontend workflows that need normalized color formats.
  name: Convert HEX to RGB/HSL API
  slug: dosvak-color-convert
- description: Colorize grayscale or desaturated images with natural, warm, cool, or sepia palettes. Returns a binary image for photo restoration and stylized previews.
  name: Colorize Image API
  slug: dosvak-colorize
- description: Compare two texts with a 0-1 similarity score, or rank candidate texts against a query by semantic relevance.
  name: Compare and Rank Text Similarity API
  slug: dosvak-compute-text-similarity
- description: Look up climate exposure for a latitude and longitude, with an optional radius. Useful for mapping, insurance, real-estate, and risk workflows.
  name: US Climate Exposure API
  slug: dosvak-coordinate-climate-exposure
- description: Get a climate score for any latitude and longitude. Useful for location ranking, site selection, travel, and geographic analytics.
  name: US Climate Risk Score API
  slug: dosvak-coordinate-climate-score
- description: Enrich latitude and longitude coordinates with location data in JSON. Useful for maps, analytics, and apps that need context for a point.
  name: US County Lookup by Coordinates API
  slug: dosvak-coordinate-enrichment
- description: Look up county climate information from a 5-digit FIPS code. Useful for geospatial enrichment, regional reporting, and county-based analytics.
  name: US County Climate Profile API
  slug: dosvak-county-climate-profile
- description: Look up place context from a 5-digit county FIPS code. Returns JSON for county-level enrichment, filters, and reference data workflows.
  name: US County Place Context API
  slug: dosvak-county-place-context
- description: Fetch a county profile by 5-digit FIPS code. Useful for demographic enrichment, reporting, and county-level lookup workflows.
  name: US County Profile API
  slug: dosvak-county-profile
- description: Crawl a website and extract emails, phones, addresses, business names, named entities, and social profiles for lead enrichment.
  name: Extract Website Contact Info API
  slug: dosvak-crawl-contact-signals
- description: Break a cron expression into labelled minute, hour, day, month, and weekday fields. Useful for schedule previews, editors, and logs.
  name: Describe Cron API
  slug: dosvak-cron-describe
- description: Compute the next fire times for a 5-field cron expression. Returns the original expression and an array of upcoming timestamps.
  name: Schedule Cron API
  slug: dosvak-cron-next
- description: Format an ISO datetime string with a Python strftime pattern. Returns the input, format, and formatted result for logs, exports, and displays.
  name: Format Date API
  slug: dosvak-date-format
- description: Get the current date and time as ISO and Unix values, with an optional time zone. Useful for scheduling, logging, and timestamp normalisation.
  name: Get Current Time API
  slug: dosvak-date-now
- description: Sharpen JPEG, PNG, or WebP images with adaptive unsharp mask processing. Tune strength and get a binary deblurred image back.
  name: Deblur Image API
  slug: dosvak-deblur-image
- description: Decrypt Fernet ciphertext with a matching key and get plaintext back. Useful for backend workflows, debugging, and verifying encrypted payloads.
  name: Decrypt Text API
  slug: dosvak-decrypt
- description: Analyze an uploaded image and get face-by-face age ranges, gender, scores, and bounding boxes. Useful for image moderation and demographic tagging.
  name: Detect Age and Gender API
  slug: dosvak-detect-age-gender
- description: Check whether an email uses a known disposable domain. Returns the email, domain, and a disposable boolean for signup and fraud filtering.
  name: Disposable Email Checker API
  slug: dosvak-detect-disposable-email
- description: Send an image file and get face bounding boxes back with face_count and image_size. Useful for cropping, overlays, and image workflows.
  name: Detect Faces from Image File API
  slug: dosvak-detect-faces
- description: Inspect a binary file's magic bytes to return filename, extension, MIME type, and description. Useful for validating uploads and classifying files reliably.
  name: Detect File type API
  slug: dosvak-detect-file-type
- description: Check whether an uploaded image is blurry and get a Laplacian variance score, threshold, and confidence. Useful for upload QA and OCR prechecks.
  name: Detect Image Blur API
  slug: dosvak-detect-image-blur
- description: Detect the language of short text and get an ISO 639-1 code with probability breakdowns. Useful for routing, translation, and multilingual processing.
  name: Detect Text Language Probabilities API
  slug: dosvak-detect-text-language
- description: Classify short text as toxic or not and get a label, score, and boolean verdict. Useful for moderating comments, chats, and user-generated content.
  name: Detect Text Toxicity API
  slug: dosvak-detect-toxicity
- description: Resolve A, AAAA, MX, TXT, NS, CNAME, SOA, PTR, and CAA records for a domain. Returns records, ttl, and any lookup error.
  name: DNS Lookup API
  slug: dosvak-dns-lookup
- description: Look up a domain's WHOIS creation date and age in days or years. Useful for onboarding, fraud review, and SEO enrichment.
  name: Calculate Domain Age API
  slug: dosvak-domain-age
- description: Get a domain’s WHOIS record from a domain query. Returns registrar, expiry date, creation date, status, emails, name servers, and more.
  name: Domain WHOIS Lookup API
  slug: dosvak-domain-whois
- description: Check an email address for syntax, MX records, and disposable domains. Get a score, level, and boolean checks to filter bad addresses early.
  name: Email Deliverability Score API
  slug: dosvak-email-deliverability-score
- description: Embed a hidden watermark into an image using a source file and watermark image. Returns the processed image as binary output.
  name: Apply Invisible Watermark on Image API
  slug: dosvak-embed-invisible-image-watermark
- description: Embed an invisible text watermark in an image and get the processed file back. Useful for tracking asset ownership without altering the visible image.
  name: Apply Invisible Text Watermark on Image API
  slug: dosvak-embed-invisible-text-watermark
- description: Encrypt a text string with Fernet and get back ciphertext, plus the key used if you omit one. Useful for protecting sensitive payloads in apps.
  name: Encrypt Text API
  slug: dosvak-encrypt
- description: Expand one keyword into related suggestions with scores and pair counts. Useful for SEO research, content planning, and ad group expansion.
  name: Expand Related Keywords API
  slug: dosvak-expand-keyword-into-related-keywords
- description: Fetch a URL and get cleaned article text with title, length, final URL, and content type. Useful for indexing, research, and content pipelines.
  name: Extract Article Text API
  slug: dosvak-extract-article-text
- description: Extract a heuristic hair region from a portrait image and return a transparent binary image. Useful for avatar, retouching, and compositing workflows.
  name: Extract Hair Region from Image API
  slug: dosvak-extract-hair-region
- description: Extract the head and shoulders from a portrait image and get a transparent image back. Useful for avatars, profile photos, and photo cutouts.
  name: Extract Head Region from Image API
  slug: dosvak-extract-head-region
- description: Extract main article text and title from HTML using readability algorithms. Returns cleaned content, short title, and length for crawlers and reading apps.
  name: Extract Readable Content from HTML API
  slug: dosvak-extract-html-readable-content
- description: Extract clean text from raw HTML, with optional URL support for better results. Returns text and length for scraping, indexing, and NLP pipelines.
  name: Extract Text from HTML API
  slug: dosvak-extract-html-text
- description: Extract a dominant hex colour and sorted palette from an uploaded image. Useful for theme generation, design workflows, and image analysis.
  name: Extract Image Color Palette API
  slug: dosvak-extract-image-palette
- description: Extract an invisible watermark from a watermarked PNG image up to 20 MB. Returns the recovered result as binary data for downstream checks.
  name: Extract Invisible Watermark from Image API
  slug: dosvak-extract-invisible-image-watermark
- description: Extract hidden text from watermarked PNG images. Returns the decoded text and bytes processed for asset review, provenance checks, or forensics.
  name: Extract Invisible Text Watermark from Image API
  slug: dosvak-extract-invisible-text-watermark
- description: Extract people, organisations, locations, and misc entities from short text. Returns offsets and confidence scores for UI highlighting and NLP pipelines.
  name: Extract Named Entities from Text API
  slug: dosvak-extract-named-entities
- description: Extract tables from a PDF file and get them back as row arrays, grouped by page and table index, with a total table count.
  name: Extract Table from PDF Document API
  slug: dosvak-extract-pdf-tables
- description: Extract text from a PDF file and receive document text, page count, and per-page text. Useful for search, review, and document automation.
  name: Extract Text from PDF Document API
  slug: dosvak-extract-pdf-text
- description: Restore and sharpen faces in an image without changing its resolution. Upload a binary image file and receive an enhanced image back.
  name: Restore and Sharpen Faces API
  slug: dosvak-face-restoration
- description: Enhance detected face regions in an uploaded image and get a restored binary image back. Useful for portrait cleanup and low-quality photo repair.
  name: Restore and enhance detected face regions API
  slug: dosvak-face-restore
- description: Generate 1 to 50 fake street addresses as plain strings. Useful for test data, sample forms, and staging datasets without real address records.
  name: Generate Fake Address API
  slug: dosvak-fake-address
- description: Generate fake company records with name, email, website, phone, and industry. Use it for test data, demos, and seeded development environments.
  name: Generate Fake Company's Info API
  slug: dosvak-fake-company
- description: Generate 1 to 50 fake person profiles with names, contact details, addresses, usernames, and DOBs for testing and demos.
  name: Generate Fake Person Info API
  slug: dosvak-fake-person
- description: Create QR code images from text or URLs with optional logo overlay and color controls. Returns binary output for branded print and digital use.
  name: Generate Branded QR Code API
  slug: dosvak-generate-branded-qr-code
- description: Generate a daily horoscope for a zodiac sign and date. Returns overview, love, career, health, lucky color, and lucky number.
  name: Generate Daily Horoscope API
  slug: dosvak-generate-daily-horoscope
- description: Generate one or more images from a text prompt. Returns base64 or normalized image results with size, model, and job metadata.
  name: Generate Text to Image API
  slug: dosvak-generate-images
- description: Generate a Janmpatri/Kundli PDF from name, birth date, birth time, coordinates, and timezone. Returns a binary PDF for astrology reports.
  name: Generate Janmpatri/Kundli PDF API
  slug: dosvak-generate-kundli-pdf
- description: Capture a PNG screenshot of any URL with optional size and wait controls. Useful for QA, archiving, and visual checks.
  name: Generate Sized Screenshot API
  slug: dosvak-generate-screenshot
- description: Hash a text string with MD5, SHA1, SHA256, or SHA512. Get the original input, chosen algorithm, and computed hash for checksums and digests.
  name: Generate Hash API
  slug: dosvak-hash
- description: Generate a PDF from HTML or a public URL, choose A4, Letter, or Legal, and merge extra PDF URLs into the output.
  name: Convert URL/HTML to PDF API
  slug: dosvak-html-to-pdf-render
- description: Remove masked objects or blemishes from an image using telea or ns inpainting. Send a source image and mask, get back a cleaned binary image.
  name: Retouching and Object Removal from Image API
  slug: dosvak-inpaint
- description: Resolve an IP to ASN, network CIDR, registry, and network name via RDAP. Useful for enrichment, abuse checks, and network telemetry.
  name: IP ASN Lookup API
  slug: dosvak-ip-asn-lookup
- description: Look up a website IP with an optional result limit. Useful for IP-based enrichment, routing, logging, and geolocation workflows.
  name: Lookup Websites by IP  API
  slug: dosvak-ip-reverse-lookup
- description: Assess an IP with a heuristic risk score, flags, ASN details, and country code. Useful for login protection, fraud screening, and abuse detection.
  name: Score IP Risk API
  slug: dosvak-ip-risk-score
- description: Encode JSON payloads into JWTs and verify tokens with a shared secret. Returns a signed token, or validity plus decoded payload.
  name: Encode and Decode JWT API
  slug: dosvak-jwt-encode-decode
- description: Get language distribution data with an optional country code and result limit. Useful for localisation, market analysis, and reference-data lookups.
  name: Get Language Breakdown Used on Web
  slug: dosvak-language-distribution
- description: Convert uploaded office documents to PDF, DOCX, TXT, and other formats. Returns the converted file as binary for downstream workflows.
  name: Convert Document with LibreOffice API
  slug: dosvak-libreoffice-document-convert
- description: List counties with optional state_name and limit filters. Useful for address forms, regional lookups, and US geography reference data.
  name: US County Directory API
  slug: dosvak-list-counties
- description: Look up a U.S. bank by 9-digit routing number. Use it to validate payment details and retrieve the routing lookup response.
  name: US Routing Number Lookup API
  slug: dosvak-lookup-bank-by-routing-number
- description: Look up authority-style metrics for a domain and get score fields plus source data. Useful for SEO analysis, outreach prioritisation, and competitor research.
  name: Domain Authority Checker API
  slug: dosvak-lookup-domain-authority-metrics
- description: Generate placeholder paragraphs with configurable paragraph count and sentences per paragraph. Returns text and paragraphs for mockups, UIs, and test content.
  name: Generate LoremIpsum API
  slug: dosvak-lorem-ipsum
- description: Combine two or more uploaded PDFs into a single binary file. Useful for bundling reports, invoices, or scanned pages into one document.
  name: Merge Multiple Documents to PDF API
  slug: dosvak-merge-pdf-files
- description: Search places by category around a latitude and longitude, with optional radius and result limits. Useful for maps, travel, and local discovery apps.
  name: Find Nearby Places in US  by Category API
  slug: dosvak-nearby-places-by-category
- description: Find places near a latitude and longitude, with optional radius and result limit. Useful for local search, maps, and location-aware apps.
  name: Find Nearby places In US API
  slug: dosvak-nearby-places
- description: Find the nearest major road segment for a latitude and longitude pair. Useful for map matching, routing, and cleaning GPS points.
  name: Find Nearest Road Segment in US API
  slug: dosvak-nearest-major-road-segment
- description: Fetch active NOAA weather alerts for a two-character area code. Useful for dashboards, notifications, and location-aware weather checks.
  name: Retrieve NOAA Weather Alerts API
  slug: dosvak-noaa-active-alerts-by-area
- description: Look up NOAA point metadata from latitude and longitude. Useful for coordinate-based location enrichment and weather-related workflows.
  name: Retrieve NOAA Weather Point Metadata API
  slug: dosvak-noaa-point-metadata
- description: Extract text from an image and get word-level bounding boxes, confidence scores, and word count. Useful for OCR pipelines, search, and document digitization.
  name: Advanced Image OCR API
  slug: dosvak-ocr-image
- description: Restore old or faded photos from an uploaded image. Control enhancement strength and scratch repair, and receive the restored image as binary output.
  name: Restore old or faded photos API
  slug: dosvak-old-photo-restore
- description: Optimize resume text or uploaded PDF/DOCX files with optional target skills. Useful for tailoring a CV to a specific role or job description.
  name: Resume Optimize Document API
  slug: dosvak-optimize-resume
- description: Parse a free-form address line and optionally a country code into a structured response. Useful for checkout, CRM cleanup, and address validation workflows.
  name: Parse & Normalize US Address API
  slug: dosvak-parse-and-normalize-address
- description: Parse resume files or text into structured output for ATS, screening, and candidate data workflows.
  name: Resume Parsing & Analysis API
  slug: dosvak-parse-resume-analyze
- description: Generate cryptographically secure passwords with configurable length and optional symbols. Returns the password and length for signup and admin workflows.
  name: Generate Password API
  slug: dosvak-password-generate
- description: Score a password by length, complexity, and common-password checks. Returns score, max, level, and per-rule checks for signup and reset flows.
  name: Check Password Strength API
  slug: dosvak-password-strength
- description: Look up a phone number’s carrier, region, time zones, and number type. Useful for contact validation, routing, and phone metadata enrichment.
  name: Phone Carrier Lookup API
  slug: dosvak-phone-carrier-lookup
- description: Parse a phone number into E.164, international, and national formats. Returns validity plus country and region details for storage and display.
  name: Phone Number Formatter API
  slug: dosvak-phone-number-format
- description: Find places inside a latitude-longitude box, with optional result limits. Useful for map search, regional filtering, and place discovery.
  name: Find US Places in Bounding Box API
  slug: dosvak-places-in-bounding-box
- description: Enhance a portrait image with contrast, smoothing, and brightness controls. Returns the edited image as binary output for upload or further processing.
  name: Portrait Photo Enhancement API
  slug: dosvak-portrait-beauty-enhancement
- description: Send text and optional language code, and get a profanity analysis back. Useful for moderating comments, chats, reviews, and other user-generated content.
  name: CheckText Profanity API
  slug: dosvak-profanity-check
- description: Segment objects from an image using a point prompt or bounding box. Returns RLE masks, scores, and prompt details for vision workflows.
  name: Prompted Image Segmentation API
  slug: dosvak-prompted-segmentation
- description: Generate PNG QR codes from text or URLs. Set image size and get a binary QR code response for labels, checkout flows, and print materials.
  name: Generate Simple QR Code API
  slug: dosvak-qr-code
- description: Generate a cryptographically secure integer between min and max. The response returns the chosen value and the range used.
  name: Generate Random Number API
  slug: dosvak-random-number
- description: Generate random strings up to 256 characters with alpha, alphanumeric, numeric, or hex output. Useful for test data, tokens, and placeholder IDs.
  name: Generate Random String API
  slug: dosvak-random-string
- description: Convert a CSV string into a JSON array of objects keyed by the header row. Get parsed rows in data and a total count for imports and data pipelines.
  name: Convert Raw CSV to JSON API
  slug: dosvak-raw-csv-to-json
- description: Convert a JSON array of objects into a CSV string with auto-generated headers. Useful for exports, reports, and spreadsheet-friendly data interchange.
  name: Convert Raw JSON to CSV  API
  slug: dosvak-raw-json-to-csv
- description: Convert a JSON object in data to a well-formed XML string, with an optional root tag. Useful for legacy integrations and format conversion.
  name: Convert Raw JSON to XML API
  slug: dosvak-raw-json-to-xml
- description: Convert XML strings into JSON while preserving attributes and text. Useful for parsing feeds, legacy integrations, and backend data normalization.
  name: Convert Raw XML to JSON API
  slug: dosvak-raw-xml-to-json
- description: Restore a stretched image to a target aspect ratio. Send an image file and get corrected binary output for cleanup and publishing workflows.
  name: Change Image Aspect Ratio API
  slug: dosvak-restore-image-aspect-ratio
- description: Smooth and sharpen a portrait image from a binary file upload. Returns the edited image for profile photos, avatars, and staff pictures.
  name: Portrait Photo Retouch API
  slug: dosvak-retouch-portrait-photo
- description: Convert latitude and longitude into a location lookup result. Useful for maps, delivery events, and turning coordinates into address context.
  name: Lookup US Address by Coordinates API
  slug: dosvak-reverse-address-lookup
- description: Convert latitude and longitude into location data, with optional points of interest. Useful for map pins, GPS events, and location-aware apps.
  name: Reverse Geocode US Coordinates API
  slug: dosvak-reverse-geocode
- description: Reverse geocode lat/lon coordinates with an optional search radius. Get a flexible JSON result for map, delivery, and GPS workflows.
  name: US Reverse Location Lookup API
  slug: dosvak-reverse-location-lookup
- description: Score uploaded images for composition and visual quality. Returns an overall score, face count, and metrics for color, thirds, exposure, and sharpness.
  name: Score Image Quality API
  slug: dosvak-score-image-aesthetic-quality
- description: Score a single image file for exposure quality and clipping. Get numeric exposure metrics and recommendations for automated photo review.
  name: Score Image Exposure API
  slug: dosvak-score-image-exposure
- description: Score two people from names and birth dates. Returns compatibility_score, summary, strengths, cautions, and per-person numerology values.
  name: Check Numerology Compatibility API
  slug: dosvak-score-numerology-compatibility
- description: Screen resumes from text or uploaded PDF/DOCX files using minimum years and required skills. Use it to automate first-pass candidate review.
  name: Skill Based Resume Screening API
  slug: dosvak-screen-resume
- description: Search address matches from a text query, with optional country filtering and result limits. Useful for autocomplete, lookup, and address validation flows.
  name: Search US Address API
  slug: dosvak-search-addresses
- description: Search counties by query with an optional limit. Useful for autocomplete, location lookup, and county-level climate data matching.
  name: US County Climate Search API
  slug: dosvak-search-climate-counties
- description: Lookup county matches from a text query, with optional result limiting. Useful for address workflows, jurisdiction checks, and location search.
  name: US County Search API
  slug: dosvak-search-counties
- description: Find domains by keyword intent. Returns ranked domains with score, matched keywords, and total hits for search and naming workflows.
  name: Search Domains by Keyword API
  slug: dosvak-search-domains-by-keyword-intent
- description: Search places with a query string and optional result limit. Useful for place lookup, map search, and location autocomplete.
  name: Search US Places API
  slug: dosvak-search-places
- description: Search and verify US trademarks by name via API. Get status, jurisdiction, ownership transfer history, and portfolio analytics for brand clearance.
  name: US Trademark Registry & Analytics API
  slug: dosvak-search-trademark-records
- description: Search, retrieve, and analyze US patent data via API. Full-text claims search, CPC classifications, citations, assignees, and yearly trend analytics.
  name: US Patent Search & Records API
  slug: dosvak-search-uspto-patents
- description: Find domains related to a given website, with an optional result limit. Useful for SEO research, competitor discovery, and prospecting.
  name: Find Similar Sites by  Domains API
  slug: dosvak-similar-domains
- description: Send a prompt with optional model, max_tokens, temperature, and system_prompt. Get back the model reply, usage, and raw completion data.
  name: Simple Chat Prompt API
  slug: dosvak-simple-chat
- description: Smooth skin-toned regions in a portrait image while preserving edges. Send a binary image and get a processed image back, with adjustable strength.
  name: Skin Smoothing API
  slug: dosvak-skin-beauty
- description: Crop a binary image around faces or the most salient area. Set aspect ratio and padding, then receive the cropped image back.
  name: Crop image around faces API
  slug: dosvak-smart-crop
- description: Detect misspellings in short text and return corrected output plus word-level replacements. Useful for editors, forms, and messaging workflows.
  name: Correct Text Spelling API
  slug: dosvak-spellcheck-text
- description: Detect misspelled words in text and get correction suggestions. Returns the original input, misspelled words, and a corrections map.
  name: Check Spelling API
  slug: dosvak-spellcheck
- description: Get climate information for a U.S. state by full name. Useful for location-aware apps, regional dashboards, and state-level lookups.
  name: US State Climate Summary API
  slug: dosvak-state-climate-summary
- description: Get state-level summary records with an optional limit up to 100. Useful for dropdowns, dashboards, and lightweight reference data lookups.
  name: US State Summary API
  slug: dosvak-state-summaries
- description: Summarize a text block and get the summary, length metrics, and compression ratio. Useful for articles, notes, and review workflows.
  name: Text Summarization API
  slug: dosvak-summarize-text-api
- description: Fetch a URL and get an extractive summary with title and length metrics. Useful for article previews, digests, and content workflows.
  name: Extract Article Summary API
  slug: dosvak-summarize-url-content
- description: Convert a datetime string between two IANA timezones. Returns the original input and converted result for scheduling and timestamp normalization.
  name: Convert Timezone API
  slug: dosvak-timezone-convert
- description: List all IANA timezone names or filter them by keyword. Returns a timezones array for scheduling, forms, and reference-data lookups.
  name: Timezones List API
  slug: dosvak-timezone-list
- description: Get the top domains for a country, sorted by coverage or rank. Useful for SEO, market research, and tracking local web popularity.
  name: Get Top Domains by Country API
  slug: dosvak-top-domains-by-country
- description: Get a ranked list of high-risk counties, with an optional limit up to 200. Useful for climate dashboards, planning tools, and location analysis.
  name: US Top Climate Risk Counties API
  slug: dosvak-top-risk-counties
- description: Search patents and trademarks in one query. Track ownership transfers and assignment history across US patent and trademark records via API.
  name: US Patent & Trademark Assignments API
  slug: dosvak-unified-uspto-search
- description: Convert a numeric value from one unit to another using value, from_unit, and to_unit. Returns the original units plus the converted result.
  name: Convert Units API
  slug: dosvak-unit-convert
- description: Resolve shortened URLs to their destination. Control redirect hops and timeout for link checks, moderation, analytics, and URL normalization.
  name: Resolve Short URL API
  slug: dosvak-unshorten-url
- description: Upscale JPEG, PNG, WebP, or BMP images by 2x or 4x and return a binary file. Optional anime mode and face enhancement support.
  name: Advanced Image Upscaler API
  slug: dosvak-upscale-image
- description: Fetch USGS earthquake records for a date range, with optional magnitude and result limits. Useful for alerts, dashboards, and seismic analysis.
  name: Retrieve USGS Earthquake Data API
  slug: dosvak-usgs-earthquakes
- description: Generate version 1 or 4 UUIDs with a single GET request. Returns the UUID string and version for database keys, tests, and distributed systems.
  name: Generate UUID API
  slug: dosvak-uuid
- description: Validate an email address by syntax only and get the local part, domain, and valid flag back. Useful for fast format checks before signup or storage.
  name: Email Syntax Validator API
  slug: dosvak-validate-email-syntax
- description: Validate an IBAN from a query parameter and use the result to catch invalid bank account numbers before payments or onboarding.
  name: Validate IBAN Checksum API
  slug: dosvak-validate-iban-checksum
- description: Validate a 9-digit U.S. routing number from a query parameter. Use it to reject invalid bank details before ACH or payment processing.
  name: US Routing Number Validation API
  slug: dosvak-validate-routing-number
- description: Audit a website for TLS, security headers, cookie flags, and basic exposure issues. Returns a score, findings, and remediation hints.
  name: Audit Website Security API
  slug: dosvak-website-security-audit
- description: Fetch World Bank indicator series by country and date range. Useful for GDP, population, and other development metrics in apps and dashboards.
  name: Retrieve World Bank Public Data API
  slug: dosvak-world-bank-indicator-series
- description: Fraudox OSINT analyzes an email address and an IP address in one request, then returns a risk-focused decision you can use in signup, lead, or abuse workflows. Send an email and an ip, and you get bac
  name: Email and IP Risk Analyzer
  slug: egemenkto-analyze-email-ip
- description: Auto-rotate PDF pages with OCR and track job progress. Returns job IDs, status, progress, and corrected PDF downloads.
  name: Fix PDF Orientation API
  slug: flowdocs-auto-correct-pdf-pages
- description: Convert .xlsx, .xlsm, and .xls files into PDF jobs. Track status, progress, and batch completion, then download finished files.
  name: Convert Excel to PDF Job API
  slug: flowdocs-convert-excel-to-pdf
- description: Convert PDF files to .xlsx workbooks and track each job by status and progress. Useful for turning invoices, reports, and statements into spreadsheets.
  name: Convert PDF to Excel Job API
  slug: flowdocs-convert-pdf-to-excel
- description: Convert PDF files to Word .docx outputs and track each job by status and progress. Supports single-file downloads and aggregated job monitoring.
  name: Convert PDF to Word Job API
  slug: flowdocs-convert-pdf-to-word
- description: Deskew scanned PDF pages and track each job by status and progress. Get corrected PDFs back as binary output for cleanup and indexing workflows.
  name: Deskew PDF API
  slug: flowdocs-deskew-pdf-pages
- description: Convert .docx, .doc, .rtf, and .odt files to PDF and track each job by status and progress. Useful for batch document workflows and downloads.
  name: Convert Word to PDF Job API
  slug: flowdocs-generate-word-to-pdf
- description: Split .xlsx and .xlsm files into one workbook per value group. Track job status, progress, and download finished split outputs.
  name: Split Excel API
  slug: flowdocs-split-excel
- description: Analyze CSV text or records for cleanup and duplicate checks. Configure key, required, and numeric columns before loading data into your system.
  name: CSV & JSON Data Cleaning and Deduplication
  slug: giacomo-petrioli-analyze
- description: 'PlaySocket Game Generator gives you a GraphQL endpoint that creates puzzle and brain-game boards for Sudoku, Schulte Table, and Stroop Table use cases. Send a query in body.query, and optionally pass '
  name: PlaySocket Puzzle & Brain Games API
  slug: gyanesh5009-playsocket-game-engine
- description: Parse ingredient text into additives, allergens, trace warnings, and dietary flags. Useful for food labels, compliance checks, and catalog enrichment.
  name: Ingredient Parser From Text API
  slug: ingredients-parse-ingredients
- description: Create speech from text and list available audio models. Compare TTS and STT capabilities, limits, pricing, and formats.
  name: Advanced Text to Speech API
  slug: llmapi-gateway-audio-text-speech
- description: Create chat responses from messages with support for tools, streaming, web search, and structured output. Returns choices plus token and cost usage.
  name: Advanced Chat Completion Generation API
  slug: llmapi-gateway-chat-completions-api
- description: Generate images from text prompts with Flux.1-Schnell or SDXL-Turbo. Poll task status for progress, errors, and the finished output URL.
  name: Generate Text to Image Job API
  slug: mastera-ai-image-generation
- description: 'Cloud Server Catalog gives you a searchable inventory of cloud locations and server offerings across providers. Use it to look up provider, region, zone, instance type, pricing, CPU and memory specs, '
  name: Compare Features & Costs across Cloud Providers
  slug: multicloud-get-field-values
- description: Analyze a web article from a URL and get entities, SEO score, content type, reading level, tone, and quality signals for review or automation.
  name: Extract and Analyze Content from Web Page API
  slug: namastesumalya-analyze-an-article
- description: Analyze resume history into trajectory, career gaps, pivots, and a loyalty score. Useful for recruiter screening and candidate review workflows.
  name: Career Trajectory and Loyalty API
  slug: namastesumalya-analyze-candidate-career-trajectory
- description: Analyze a webpage URL for keywords, sentiment, readability, language, and word count. Useful for SEO audits and content review workflows.
  name: Content and Keyword Analysis API
  slug: namastesumalya-analyze-content-keywords
- description: Compare a list of website URLs and get an overall similarity score, per-site SEO scores, AI summaries, and improvement suggestions.
  name: Advanced Website Similarity Analysis API
  slug: namastesumalya-analyze-website-similarity
- description: Audit a URL’s security headers and get a score, header status, and recommendations. Useful for checking CSP, HSTS, and other browser protections.
  name: Security Header Full Audit API
  slug: namastesumalya-audit-website-security-headers
- description: Compare multiple article URLs and get shared themes, topic overlap, style differences, structural contrast, and perspective analysis.
  name: Extract and Compare Multiple Articles from Web Pages API
  slug: namastesumalya-compare-multiple-articles
- description: Compare two resumes against a job title and get a winner, rationale, and skill-by-skill matrix for hiring review and shortlist ranking.
  name: Candidate Comparison API
  slug: namastesumalya-compare-two-candidates-head-to-head
- description: Estimate a candidate’s market salary range from job title, location, and resume content. Returns market context plus min, max, and currency.
  name: Global Salary Benchmark API
  slug: namastesumalya-estimate-market-salary-range
- description: Rank resume summaries against a job title and return topCandidates plus an executiveReport. Useful for fast HR screening and shortlist review.
  name: Advanced Shortlist API
  slug: namastesumalya-executive-level-shortlist
- description: Extract article text and metadata from a URL or a batch of URLs. Returns title, author, word count, reading time, and publication details when available.
  name: Extract Article Content from Web Page API
  slug: namastesumalya-extract-article-content
- description: Extract metadata from a single URL or a batch of URLs. Useful for link previews, crawling, SEO audits, and content indexing.
  name: Extract Metadata From URL API
  slug: namastesumalya-extract-metadata-from-url-api
- description: Extract technical skills, soft skills, certifications, and experience years from resume text for ATS parsing, candidate scoring, and profile enrichment.
  name: Skill Extraction API
  slug: namastesumalya-extract-skills
- description: Check a URL for schema markup and get structuredData, schemaCount, hasBreadcrumbs, and hasOrganization back for SEO audits and automation.
  name: Extract Structured Data API
  slug: namastesumalya-extract-structured-data
- description: Analyze a website URL for key market trends, opportunity score, differentiation, and growth potential. Useful for product research and competitor review.
  name: Market Trends and Growth Forecasting API
  slug: namastesumalya-forecast-market-trends
- description: Generate interview questions and target answers from a job title and resume content. Useful for structured hiring prep tied to a candidate's background.
  name: Interview Prep Pack API
  slug: namastesumalya-generate-a-tailored-interview-prep-pack
- description: Generate country-specific subscription price recommendations from a base price, currency, and home country. Returns local prices and justification.
  name: Global Pricing Recommendations API
  slug: namastesumalya-generate-global-pricing-recommendations
- description: Generate a full job description from a role title and requirements. Returns ATS, LinkedIn, and interview scorecard versions for hiring teams.
  name: Job Description Generator API
  slug: namastesumalya-generate-job-description
- description: Group keywords from an article URL into topic clusters, a primary topic, and related keywords for SEO and content analysis.
  name: Generate Keyword Clusters API
  slug: namastesumalya-generate-keyword-clusters
- description: Summarize multiple URLs into one digest with sources, a summary, and key takeaways. Useful for newsletter workflows, research briefs, and content review.
  name: Extract and Generate Editorial Digest from Multiple Web Pages API
  slug: namastesumalya-generate-newsletter-digest
- description: Identify a website's competitors from a URL. Get industry, market niche, overlap scores, and a differentiation strategy for research and outreach.
  name: Intelligent Competitor Mapping API
  slug: namastesumalya-identify-competitors
- description: Rewrite a resume for a target job title and get before/after ATS scores, an improved version, and added keywords.
  name: Resume Optimizer (ATS) API
  slug: namastesumalya-optimize-resume-ats
- description: Check a webpage URL for canonical, robots.txt, SSL status, and performance scores. Get issues and overall score for technical SEO review.
  name: Webpage Technical Performance Audit API
  slug: namastesumalya-perform-technical-performance-audit
- description: Score a resume against a job title and get strengths, gaps, verdict, and security risk notes. Rank multiple candidates for hiring workflows.
  name: Resume Screening API
  slug: namastesumalya-resume-screening-api
- description: Review job description text for bias and inclusion issues. Returns a winner, rationale, and comparison matrix for hiring copy checks.
  name: Bias and Inclusion Scan API
  slug: namastesumalya-scan-bias-and-inclusion
- description: Summarize one article or batch article URLs from body.urls. Useful for digests, research workflows, and content review.
  name: Summarize Multiple Article Insights API
  slug: namastesumalya-summarize-multiple-article-insights-api
- description: Compare multiple website URLs and get technical SEO data for each page, including metadata, headings, links, accessibility, and load time.
  name: Technical Comparison of Webpages API
  slug: namastesumalya-technical-comparison
- description: Translate a web article from its URL into a target language. Returns translated title, author, publication name, and body.
  name: Extract and Translate Article Content from Web Page API
  slug: namastesumalya-translate-article-content
- description: Validate address input from query params or JSON body. Returns `success`, `code`, and additional module blocks for basic address checks.
  name: Address Validation & Location Lookup API
  slug: quadlem-address-validation
- description: Validate a BIN against an IP address and get a simple response envelope with `success` and `code`. Useful for fraud checks and payment routing.
  name: BIN IP Checker API
  slug: quadlem-bin-ip-checker
- description: Look up a card BIN from a single query parameter and get a success envelope with a code. Useful for payment routing, analytics, and fraud checks.
  name: BIN Lookup API
  slug: quadlem-bin-lookup
- description: Search BIN records by bank, brand, country, prefix, level, or card type. Get a response envelope with a success flag, code, and module blocks.
  name: Search & Filter BIN Database API
  slug: quadlem-bin-search
- description: Verify companies by LEI, VAT, name, and country. Get a JSON envelope with success status and lookup results for KYB and onboarding checks.
  name: Company KYB Lookup API
  slug: quadlem-company-kyb-lookup
- description: Verify an email address from a single query parameter and get a response with code and success. Useful for signup checks and list cleanup.
  name: Advanced Email Verification API
  slug: quadlem-email-verification
- description: Get FX rate data for a chosen base currency. Returns a success flag, numeric code, and the rate blocks used in pricing, billing, and reporting.
  name: Foreigen Exchange Rates API
  slug: quadlem-fx-rates
- description: Validate an IBAN from a single iban parameter and get a success/code response. Useful for payment flows and bank-detail checks.
  name: Advanced IBAN Validation API
  slug: quadlem-iban-validation
- description: Send an IP address and get a structured lookup response with success and code fields. Useful for geolocation, enrichment, and fraud checks.
  name: IP Address Lookup API
  slug: quadlem-ip-address-look-up
- description: Check a name against sanctions and AML screening data, with optional date of birth, country, and result limit filters. Returns a success flag and code.
  name: AML & Sanctions Verification API
  slug: quadlem-sanctions-screening
- description: Validate IP, BIN, DOB, VAT, IBAN, email, phone, address, and more in one request. Useful for onboarding, risk checks, and pre-validation workflows.
  name: Identity & Fraud Verification API
  slug: quadlem-verify-all-in-one
- description: Beach Information gives you searchable beach records, local rules, amenities, conditions, and tide forecasts in one API. Use it to look up beaches by country, state, or name, then pull the details you
  name: Compare Beaches Around the World
  slug: ryanvinson-beaches-information
- description: Festival Listings gives you searchable data on festivals, their categories, countries, deadlines, dates, fees, and roster details. Use the list endpoints to browse festivals with filters for q, genre,
  name: Find & Compare Film Festivals Around the World
  slug: ryanvinson-film-festivals-around-world
- description: SE Ranking Data API | AI search - analyze a domain/brand's visibility and performance within various LLM results, such as ChatGPT, Gemini, and Perplexity
  name: Analyze AI Search Performance API
  slug: se-ranking-ai-search
- description: SE Ranking Data API | Backlinks - conduct a comprehensive analysis of the backlink profile for any given target
  name: Analyze Backlinks API
  slug: se-ranking-backlinks
- description: SE Ranking Data API | Domain Analysis - perform in-depth competitive analysis on any domain
  name: Advanced Domain Analysis API
  slug: se-ranking-domain-analysis
- description: SE Ranking Data API | Keyword Research - comprehensive keyword analysis and discovery
  name: Research Keywords API
  slug: se-ranking-keyword-research
- description: SE Ranking Data API | SERP Results - retrieve the top 100 search engine results pages (SERPs) for any keyword in real-time
  name: Get SERP Results API
  slug: se-ranking-serp-results-classic
- description: SE Ranking Data API | Website Audit - provides a comprehensive suite of tools to programmatically manage the full lifecycle of your technical SEO audits
  name: Audit Website SEO API
  slug: se-ranking-website-audit
- description: Extract email addresses from text with an async job flow. Submit content, then poll for a result array of detected email strings.
  name: Detect Email Address API
  slug: sharpapi-detect-email-addresses
- description: Detect phone numbers in free-form text and poll job status for parsed_number and detected_number results. Useful for cleanup and validation workflows.
  name: Detect Phones Numbers API
  slug: sharpapi-detect-phone-numbers
- description: Submit text content for spam screening and poll job status. Returns a score, pass flag, and reason for moderation workflows.
  name: Detect Spam API
  slug: sharpapi-detect-spam
- description: Extract URLs from a content string and poll for results. Returns each detected link with its full URL and protocol.
  name: URls Detector API
  slug: sharpapi-detect-urls
- description: Generate ranked hospitality category names from travel content. Returns job status plus category names and weights for taxonomy workflows.
  name: Generate Hospitality Product Categories API
  slug: sharpapi-generate-hospitality-product-categories
- description: Generate keyword lists from a content string, with optional context, language, voice tone, and max quantity. Poll for an async result array.
  name: Generate Keywords/Tags API
  slug: sharpapi-generate-keywords-tags
- description: Generate category suggestions from product content and poll for results. Returns ranked category names with weights for catalog and SKU classification.
  name: Generate Product Categories API
  slug: sharpapi-generate-product-categories
- description: Generate a product introduction from content, with language, length, and tone options. Poll a job status URL and receive the finished product_intro.
  name: Generate Product Introduction API
  slug: sharpapi-generate-product-introduction
- description: Analyze product review text asynchronously and get back a score and opinion. Useful for moderation, feedback triage, and sentiment dashboards.
  name: Generate Product Review Sentiment API
  slug: sharpapi-generate-product-review-sentiment
- description: Generate SEO meta tags from page content, with optional language and voice tone. Returns a job ID, status URL, and meta_tags for publishing.
  name: SEO Tags Generator API
  slug: sharpapi-generate-seo-tags
- description: Generate a thank-you email from a brief, with optional language, length, context, and tone controls. Returns a job ID, status URL, and finished email.
  name: Generate Thank You E-mail API
  slug: sharpapi-generate-thank-you-email
- description: Classify travel content into ranked tours and activities categories. Returns job status plus category names and weights for search, merchandising, and taxonomy cleanup.
  name: Generate Tours & Activities Product Categories API
  slug: sharpapi-generate-tours-activities-product-catego
- description: Analyze travel review text asynchronously and get a sentiment score with POSITIVE or similar opinion output. Useful for feedback triage and review analytics.
  name: Generate Travel Review Sentiment API
  slug: sharpapi-generate-travel-review-sentiment
- description: Generate structured job descriptions from a title and hiring context. Returns requirements, responsibilities, and a short summary for HR workflows.
  name: Job Description Generator API
  slug: sharpapi-job-description-generator
- description: List job positions with ids, names, slugs, and pagination metadata. Optionally include related roles with relevancy weights for HR and hiring tools.
  name: Job Positions API
  slug: sharpapi-list-job-positions
- description: Rewrite content with optional context, language, length, and tone controls. Returns a job ID, status URL, and the paraphrased text when complete.
  name: Paraphrase Text API
  slug: sharpapi-paraphrase-text
- description: Submit invoice files and poll for structured results. Extract buyer, seller, invoice, financial totals, and line items from PDFs and images.
  name: Invoice Parsing API
  slug: sharpapi-parse-invoice
- description: Parse PDF, DOC, DOCX, TXT, or RTF resumes into structured candidate, work history, and education data. Useful for ATS intake and profile enrichment.
  name: Resume Parser API
  slug: sharpapi-parse-resume
- description: Submit text in content, get a job_id and status_url, then poll for a proofread result. Useful for cleaning drafts and user-generated copy.
  name: Proofread Text + Grammar Check API
  slug: sharpapi-proofread-text-grammar-check
- description: Generate related job titles from a role name. Submit a position, poll for results, and get weighted suggestions for recruiting or job search.
  name: Related Job Positions Generator API
  slug: sharpapi-related-job-positions-generator
- description: Generate related job positions or skills from a role name. Returns ranked results with weights via an async job status response.
  name: Related Skills Generator API
  slug: sharpapi-related-skills-generator
- description: Compare a resume file against a plain-text job description. Get match scores, explanations, and job status for recruiter screening and ATS workflows.
  name: Resume/CV Job Match Score API
  slug: sharpapi-resume-cv-job-match-score
- description: Scrape a URL and get back page content, metadata, and links in a structured response. Useful for indexing, SEO checks, and content monitoring.
  name: Web Scraping API
  slug: sharpapi-scrape-url
- description: Look up skills by name and page through a skills list. Returns skill IDs, names, slugs, related skills, and pagination metadata.
  name: Skills Database API
  slug: sharpapi-skills-database
- description: Summarize text asynchronously with optional context, language, max length, and voice tone. Returns a job ID, status URL, and final summary.
  name: Summarize Text API
  slug: sharpapi-summarize-text
- description: Submit text with optional context, source language, and voice tone. Track the job and get translated content with from/to language metadata.
  name: Translate Text API
  slug: sharpapi-translate-text
artifact_total: 468
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ApyHub Convert API
  slug: open-apyhub-convert-api
- collection_type: open
  name: ApyHub Convert Currency API
  slug: open-apyhub-currency-api
- collection_type: open
  name: ApyHub Convert Extract API
  slug: open-apyhub-extract-api
- collection_type: open
  name: ApyHub Convert Generate API
  slug: open-apyhub-generate-api
created: '2025-01-08'
description: ApyHub is a marketplace of certified, production-ready HTTP APIs. One API key and one subscription work across every service in the catalog, metered in 'atoms' (a per-call credit unit). The catalog spans 451 services from 19 providers across 21 categories - AI, file conversion and manipulation, data extraction and validation, SEO, geolocation, finance, HR and more - and is MCP-ready by default. Every page is available as Markdown by appending .md to its path.
examples:
- key_count: 7
  name: Conversion Request Example
  slug: conversion-request-example
finops:
- name: Apyhub Finops
  service_category: API
  slug: apyhub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apyhub.png
json_schemas:
- name: ConversionRequest
  property_count: 7
  slug: conversion-request
json_structures:
- name: Conversion Request Structure
  property_count: 0
  slug: conversion-request-structure
jsonld:
- class_count: 12
  name: Apyhub Context
  property_count: 0
  slug: apyhub-context
layout: provider
modified: '2026-08-18'
name: ApyHub
nav: Providers
network: true
overview: 'ApyHub publishes 210 APIs on the [APIs.io](https://apis.io/) network, including Apply Headers and Footers on DOCX API, Apply Footers on PDF API, AI Audio Language Detection API, and 207 more. Tagged areas include API Marketplace, API Platform, Utility APIs, Document Conversion, and Data Processing.


  The ApyHub catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Apyhub Plans Pricing
  plan_count: 3
  slug: apyhub-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Apyhub Rate Limits
  slug: apyhub-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: ApyHub API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: apyhub-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: ApyHub API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 13
  slug: apyhub-spectral-rules
score:
  band: thin
  composite: 26.7
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 64.3
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 210
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apyhub/refs/heads/main/screenshots/apyhub-2026-06-20T172345.png
security:
- kind: authentication
  name: Apyhub Authentication
  slug: apyhub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apyhub Domain Security
  slug: apyhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apyhub
tags:
- API Marketplace
- API Platform
- Utility APIs
- Document Conversion
- Data Processing
- Artificial Intelligence
- MCP
- Agent Ready
---
