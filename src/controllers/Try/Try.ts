import { Controller, Get, Post, Put, Delete, Body, Param } from '@nestjs/common';

@Controller('{{componentname}}')
export class TryController {

  @Get()
  findAll() {
    // TODO: return all Try
    return [];
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    // TODO: return one Try
    return {};
  }

  @Post()
  create(@Body() data: any) {
    // TODO: create Try
    return data;
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() data: any) {
    // TODO: update Try
    return data;
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    // TODO: delete Try
    return { deleted: id };
  }
}