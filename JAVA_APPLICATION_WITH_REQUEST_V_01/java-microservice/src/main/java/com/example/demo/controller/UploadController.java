package com.example.demo.controller;

import com.example.demo.model.DataEntity;
import com.example.demo.payload.DataPayload;
import com.example.demo.repository.DataRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class UploadController {

  @Autowired
  private DataRepository dataRepository;

  @PostMapping("/upload")
  public ResponseEntity<String> uploadData(@RequestBody DataPayload payload) {
    DataEntity entity = new DataEntity();
    entity.setField1(payload.getField1());
    entity.setField2(payload.getField2());
    dataRepository.save(entity);
    return ResponseEntity.ok("Data saved!");
  }
}
