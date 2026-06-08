async function try2Routes(fastify, options) {

  fastify.get('/', async (request, reply) => {
    // TODO: get all try2
    return [];
  });

  fastify.get('/:id', async (request, reply) => {
    const { id } = request.params;
    // TODO: get one try2
    return {};
  });

  fastify.post('/', async (request, reply) => {
    const data = request.body;
    // TODO: create try2
    reply.status(201).send(data);
  });

  fastify.put('/:id', async (request, reply) => {
    const data = request.body;
    // TODO: update try2
    return data;
  });

  fastify.delete('/:id', async (request, reply) => {
    const { id } = request.params;
    // TODO: delete try2
    return { deleted: id };
  });
}

module.exports = try2Routes;