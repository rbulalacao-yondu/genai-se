const mongoose = require('mongoose');

const projectSchema = new mongoose.Schema(
  {
    name: { type: String, required: true },
    owner: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    status: { 
      type: String, 
      enum: ['planning', 'active', 'completed'], 
      default: 'planning' 
    }
  },
  { timestamps: true }
);

module.exports = mongoose.model('Project', projectSchema);
