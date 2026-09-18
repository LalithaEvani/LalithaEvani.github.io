---
layout: page
title: SemiHastakshar
description: Semi-supervised Indic handwritten OCR, trained on large-scale unlabeled handwriting collected from the web.
img: assets/img/semihastakshar-teaser.png
importance: 2
category: research
related_publications: true
---

**Problem.** HTR models trained only on small, curated benchmarks struggle
to generalize to the messy variety of real-world Indic handwriting — writing
styles, scripts, and image quality vary far more "in the wild" than in any
lab dataset.

**Approach.** We collect Indic-HW-Wild, a 2.4M+-word unlabeled corpus of
real-world Indic handwriting scraped from the internet, and train with
high-confidence pseudo-labeling — iteratively re-labeling the unlabeled pool
with the current best model and retraining on the mix.

**Results.** SemiHastakshar cuts out-of-domain WER by up to 19% (Telugu)
over a PARSeq HTR baseline trained only on labeled data, published at
ICVGIP 2025 {% cite evani2025semihastakshar %}.

**Links.** [Project page](https://lalithaevani.github.io/SemiHastakshar-page/) · [Paper](https://doi.org/10.1145/3774521.3774605) · [Code](https://github.com/LalithaEvani/SemiHastakshar)

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/semihastakshar-teaser.png" title="Sample word-level images across nine Indic scripts" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Sample word-level images from Indic-HW-Wild, the unlabeled dataset behind SemiHastakshar.
</div>
