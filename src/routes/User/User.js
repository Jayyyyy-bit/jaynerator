const express = require('express');
const router  = express.Router();

// GET /{{componentname}}
router.get('/', async (req, res) => {
  try {
    // TODO: get all User
    res.json([]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// GET /{{componentname}}/:id
router.get('/:id', async (req, res) => {
  try {
    // TODO: get one User
    res.json({});
  } catch (err) {
    res.status(404).json({ error: 'Not found' });
  }
});

// POST /{{componentname}}
router.post('/', async (req, res) => {
  try {
    const data = req.body;
    // TODO: create User
    res.status(201).json(data);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// PUT /{{componentname}}/:id
router.put('/:id', async (req, res) => {
  try {
    const data = req.body;
    // TODO: update User
    res.json(data);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// DELETE /{{componentname}}/:id
router.delete('/:id', async (req, res) => {
  try {
    // TODO: delete User
    res.json({ deleted: req.params.id });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

module.exports = router;