/*! Kin Score glyph — the K'in sun.
 *  Generated from kin-glyph.js by build.mjs. Do not edit here.
 *  Canonical source: api-evangelist/kin-score/glyph/
 *  Spec: api-evangelist/kin-score/glyph/GLYPH.md
 */
(function (root) {
  'use strict';

/*
 * Kin Score glyph — the K'in sun.
 *
 * Core  : concentric rings, one per Kin Score facet, filled clockwise to that
 *         facet's score. Ring colour depends on the palette (see PALETTES).
 * Rays  : 12 triangles around the outside, one per agent-readiness dimension,
 *         solid when the dimension is satisfied — the sun's rays.
 *
 * Zero dependencies. Returns an SVG string, so it renders identically at build
 * time, at runtime, and inside a PNG pipeline.
 */

/* Each facet owns a fixed hue, in fixed order. Categorical colour encodes
   IDENTITY (which facet this is), never rank — arc length carries the score.
   This is the Apple Activity model: Move/Exercise/Stand are always red/green/
   blue however well you did. It is also what keeps the glyph colourful for
   every provider, including one scoring uniformly high, where colouring by
   band collapses to a single hue.
   Hues are slots 1-6 of the design system's validated categorical theme.
   Validated `--pairs adjacent`: ALL CHECKS PASS in both light and dark. */
const FACETS = [
  { id: 'discoverability',          label: 'Discoverability',          light: '#2a78d6', dark: '#3987e5' },
  { id: 'contract_quality',         label: 'Contract Quality',         light: '#eb6834', dark: '#d95926' },
  { id: 'governance',               label: 'Governance',               light: '#1baf7a', dark: '#199e70' },
  { id: 'operational_transparency', label: 'Operational Transparency', light: '#eda100', dark: '#c98500' },
  { id: 'developer_ergonomics',     label: 'Developer Ergonomics',     light: '#e87ba4', dark: '#d55181' },
  { id: 'commercial_clarity',       label: 'Commercial Clarity',       light: '#008300', dark: '#008300' },
];

const DIMENSIONS = [
  { id: 'spec_presence',      label: 'Machine-Readable Contract' },
  { id: 'agentic_access',     label: 'Agentic Access Contract' },
  { id: 'mcp_server',         label: 'MCP Server' },
  { id: 'auth_clarity',       label: 'Machine-Readable Auth' },
  { id: 'idempotency',        label: 'Idempotency' },
  { id: 'error_semantics',    label: 'Stable Error Semantics' },
  { id: 'openapi_examples',   label: 'Request/Response Examples' },
  { id: 'rate_limit_signal',  label: 'Rate-Limit Signaling' },
  { id: 'asyncapi_events',    label: 'Typed Event Surface' },
  { id: 'agent_skills',       label: 'Agent Skills' },
  { id: 'well_known_catalog', label: 'Well-Known Catalog' },
  { id: 'consent_identity',   label: 'Consent & Bot Identity' },
];

// Band thresholds, high → low (scoring.yml `bands`).
const BANDS = [
  { id: 'exemplar',   label: 'Exemplar',   min: 70 },
  { id: 'strong',     label: 'Strong',     min: 60 },
  { id: 'developing', label: 'Developing', min: 45 },
  { id: 'thin',       label: 'Thin',       min: 30 },
  { id: 'emerging',   label: 'Emerging',   min: 15 },
  { id: 'minimal',    label: 'Minimal',    min: 0  },
];

const PALETTES = {
  /* ORDINAL — one hue family, 38 deg traverse (cyan -> deep indigo).
     Validated --ordinal: ALL CHECKS PASS on both surfaces. Rank is readable
     from colour alone and survives greyscale — but a uniformly-strong provider
     comes out near-monochrome. */
  ordinal: {
    light: {
      surface: '#f8f9fa',
      exemplar: '#002e7b', strong: '#005295', developing: '#1575ae',
      thin: '#3999c5', emerging: '#5ebcdc', minimal: '#c2c7cf',
      track: '#dfe3e8', ink: '#12172b', muted: '#5b6270', rayOff: '#8b93a3',
    },
    dark: {
      surface: '#1a1a2e',
      exemplar: '#87dfff', strong: '#65bbe6', developing: '#4897cd',
      thin: '#3173b4', emerging: '#234f99', minimal: '#4a5162',
      track: '#343850', ink: '#f3f5f8', muted: '#9aa2b4', rayOff: '#7f88a0',
    },
  },
  /* BRIGHT — distinct hues per BAND. Easy to tell bands apart, impossible to
     rank without the legend. Light passes with reliefs; dark does not (no five
     hues in that column are mutually separable). Kept for comparison. */
  bright: {
    light: {
      surface: '#f8f9fa',
      exemplar: '#4a3aa7', strong: '#2a78d6', developing: '#1baf7a',
      thin: '#eda100', emerging: '#e34948', minimal: '#c2c7cf',
      track: '#dfe3e8', ink: '#12172b', muted: '#5b6270', rayOff: '#8b93a3',
    },
    dark: {
      surface: '#1a1a2e',
      exemplar: '#9085e9', strong: '#3987e5', developing: '#199e70',
      thin: '#c98500', emerging: '#e66767', minimal: '#4a5162',
      track: '#343850', ink: '#f3f5f8', muted: '#9aa2b4', rayOff: '#7f88a0',
    },
  },
};

/* FACET — rings take their own facet's hue (see FACETS), so the glyph is
   always full of colour. Rank moves to the centre: the band name under the
   number. Chrome (track/ink/muted) is shared with the ordinal palette. */
PALETTES.facet = {
  light: { ...PALETTES.ordinal.light },
  dark:  { ...PALETTES.ordinal.dark  },
};

/* RAYS — a warm gold ramp of their own, keyed to the agent-readiness band, so
   the sun's rays read as sunlight rather than as more of the core palette. Held
   deliberately apart from every ring hue: nothing in FACETS is warm-gold, so a
   ray can never be mistaken for a facet.
   The ramp BRIGHTENS with readiness: agent-native is the most luminous gold the
   light surface will carry (#dea800, 2.05:1 — the contrast floor is what stops
   it going brighter still), agent-aware and below fall away into amber. On dark
   it opens right up to #ffd060.
   Validated --ordinal: ALL CHECKS PASS on both surfaces. */
const RAYS = {
  light: {
    'agent-native': '#dea800', 'agent-ready': '#cf8700',
    'agent-aware':  '#bd6800', 'human-only':  '#a94900',
  },
  dark: {
    'agent-native': '#ffd060', 'agent-ready': '#e9a738',
    'agent-aware':  '#d07e0b', 'human-only':  '#b45600',
  },
};

// Back-compat.
const RAMP = PALETTES.ordinal;

function bandOf(score) {
  for (const b of BANDS) if (score >= b.min) return b.id;
  return 'minimal';
}

const esc = (s) => String(s).replace(/[&<>"]/g, (c) =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/**
 * @param {object} p     {name, score, band, agent_score, agent_band, facets, agent_dims}
 * @param {object} opts  {size, mode:'light'|'dark', palette:'facet'|'ordinal'|'bright',
 *                        showRays, coreFill, title}
 * @returns {string} SVG markup
 */
function kinGlyph(p, opts = {}) {
  const size = opts.size || 240;
  const mode = opts.mode || 'light';
  const palette = opts.palette || 'facet';
  const C = (PALETTES[palette] || PALETTES.facet)[mode];
  const showRays = opts.showRays !== false;
  const cx = size / 2, cy = size / 2;

  const rayBand = showRays ? size * 0.115 : 0;
  const outerR  = size / 2 - rayBand - size * 0.02;
  const coreR   = size * 0.163;   // room for the band label under the number
  const gap     = Math.max(2, size * 0.018);
  const ringW   = (outerR - coreR - gap * (FACETS.length - 1)) / FACETS.length;

  const parts = [];

  // --- facet rings --------------------------------------------------------
  // stroke-dasharray on a circle gives rounded data-ends and needs no arc maths.
  FACETS.forEach((f, i) => {
    const raw = Number(p.facets?.[f.id] ?? 0);
    const v = Math.max(0, Math.min(100, raw));
    const r = outerR - ringW / 2 - i * (ringW + gap);
    const circ = 2 * Math.PI * r;
    const band = bandOf(v);
    const col = palette === 'facet' ? f[mode] : C[band];

    // The TRACK carries the hover hooks, so the whole ring is hoverable —
    // including a facet scoring zero, where there is no filled arc to hit.
    const hooks =
      `data-kind="ring" data-label="${esc(f.label)}" ` +
      `data-value="${raw.toFixed(1)}" data-band="${band}"`;
    const tip = `<title>${esc(f.label)}: ${raw.toFixed(1)} (${band})</title>`;

    parts.push(
      `<circle cx="${cx}" cy="${cy}" r="${r.toFixed(2)}" fill="none" ` +
      `stroke="${C.track}" stroke-width="${ringW.toFixed(2)}" ${hooks}>${tip}</circle>`);

    if (v > 0) {
      const on = (v / 100) * circ;
      parts.push(
        `<circle cx="${cx}" cy="${cy}" r="${r.toFixed(2)}" fill="none" ` +
        `stroke="${col}" stroke-width="${ringW.toFixed(2)}" stroke-linecap="round" ` +
        `stroke-dasharray="${on.toFixed(2)} ${(circ - on).toFixed(2)}" ` +
        `transform="rotate(-90 ${cx} ${cy})" ${hooks}>${tip}</circle>`);
    }
  });

  // --- agent-readiness rays ----------------------------------------------
  if (showRays) {
    const agentBand = p.agent_band || 'human-only';
    const rayCol = RAYS[mode][agentBand] || RAYS[mode]['human-only'];
    const baseR = outerR + size * 0.022;
    const tipR = baseR + rayBand * 0.72;
    const halfW = (Math.PI * 2 * baseR) / DIMENSIONS.length * 0.30;
    // Unsatisfied rays get a heavier, darker outline than the ring track so the
    // sun's silhouette survives greyscale, print and forced-colors.
    const strokeW = Math.max(1.25, size * 0.0125);

    DIMENSIONS.forEach((d, i) => {
      const a = (i / DIMENSIONS.length) * Math.PI * 2 - Math.PI / 2;
      const on = !!p.agent_dims?.[d.id];
      const px = Math.cos(a), py = Math.sin(a), nx = -py, ny = px;
      const pts = [
        [cx + px * tipR, cy + py * tipR],
        [cx + px * baseR + nx * halfW, cy + py * baseR + ny * halfW],
        [cx + px * baseR - nx * halfW, cy + py * baseR - ny * halfW],
      ].map(([x, y]) => `${x.toFixed(2)},${y.toFixed(2)}`).join(' ');

      parts.push(
        `<polygon points="${pts}" ` +
        (on ? `fill="${rayCol}" stroke="${rayCol}" stroke-width="${(strokeW * 0.5).toFixed(2)}"`
            : `fill="none" stroke="${C.rayOff}" stroke-width="${strokeW.toFixed(2)}"`) +
        ` stroke-linejoin="round" data-kind="ray" data-label="${esc(d.label)}" data-on="${on}">` +
        `<title>${esc(d.label)}: ${on ? 'satisfied' : 'not satisfied'}</title></polygon>`);
    });
  }

  // --- core ---------------------------------------------------------------
  // The disc sits INSIDE the innermost ring (radius coreR, not coreR + gap).
  // At coreR + gap it covered 83% of that ring, hiding Commercial Clarity and
  // swallowing its hover. pointer-events="none" so it can never block a ring.
  const scoreBand = p.band || bandOf(p.score);
  parts.push(
    `<circle cx="${cx}" cy="${cy}" r="${coreR.toFixed(2)}" ` +
    `fill="${opts.coreFill || C.surface}" pointer-events="none"/>`);

  if (size >= 96) {
    const withBand = palette === 'facet';
    parts.push(
      `<text x="${cx}" y="${(cy - (withBand ? size * 0.020 : 0)).toFixed(1)}" ` +
      `text-anchor="middle" dominant-baseline="central" pointer-events="none" ` +
      `font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-weight="700" ` +
      `font-size="${(size * 0.130).toFixed(1)}" fill="${C.ink}">${Number(p.score).toFixed(1)}</text>`);
    if (withBand) {
      // Rank left the rings, so state it plainly under the number.
      parts.push(
        `<text x="${cx}" y="${(cy + size * 0.064).toFixed(1)}" text-anchor="middle" ` +
        `dominant-baseline="central" pointer-events="none" ` +
        `font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-weight="600" ` +
        `font-size="${(size * 0.038).toFixed(1)}" fill="${C.muted}" ` +
        `letter-spacing="${(size * 0.003).toFixed(2)}">${scoreBand.toUpperCase()}</text>`);
    }
  } else {
    parts.push(
      `<circle cx="${cx}" cy="${cy}" r="${(coreR * 0.55).toFixed(2)}" ` +
      `fill="${PALETTES.ordinal[mode][scoreBand]}" pointer-events="none"/>`);
  }

  const label = opts.title || `${p.name}: Kin Score ${Number(p.score).toFixed(1)} (${scoreBand}), ` +
    `agent readiness ${Number(p.agent_score || 0).toFixed(0)} (${p.agent_band || 'human-only'})`;

  return `<svg viewBox="0 0 ${size} ${size}" width="${size}" height="${size}" ` +
    `xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc(label)}">` +
    `<title>${esc(label)}</title>${parts.join('')}</svg>`;
}


  function parseJSONAttr(el, name) {
    const raw = el.getAttribute(name);
    if (!raw) return {};
    try { return JSON.parse(raw); } catch (e) { return {}; }
  }

  /** Render one placeholder element in place. */
  function render(el) {
    if (el.getAttribute('data-kin-rendered') === '1') return;
    const p = {
      name:        el.getAttribute('data-name') || '',
      score:       parseFloat(el.getAttribute('data-score') || '0') || 0,
      band:        el.getAttribute('data-band') || null,
      agent_score: parseFloat(el.getAttribute('data-agent-score') || '0') || 0,
      agent_band:  el.getAttribute('data-agent-band') || 'human-only',
      facets:      parseJSONAttr(el, 'data-facets'),
      agent_dims:  parseJSONAttr(el, 'data-dims'),
    };
    const size = parseInt(el.getAttribute('data-size') || '72', 10);
    const mode = el.getAttribute('data-mode') ||
      (document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light');
    el.innerHTML = kinGlyph(p, {
      size: size,
      mode: mode,
      palette: el.getAttribute('data-palette') || 'facet',
      showRays: el.getAttribute('data-rays') !== 'false',
      coreFill: el.getAttribute('data-core-fill') || undefined,
    });
    el.setAttribute('data-kin-rendered', '1');
  }

  function renderAll(scope) {
    const nodes = (scope || document).querySelectorAll('[data-kin-glyph]');
    for (let i = 0; i < nodes.length; i++) render(nodes[i]);
    return nodes.length;
  }

  root.KinGlyph = {
    render: render,
    renderAll: renderAll,
    svg: kinGlyph,
    FACETS: FACETS,
    DIMENSIONS: DIMENSIONS,
    BANDS: BANDS,
    PALETTES: PALETTES,
    RAYS: RAYS,
    bandOf: bandOf,
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { renderAll(); });
  } else {
    renderAll();
  }
})(typeof window !== 'undefined' ? window : globalThis);
