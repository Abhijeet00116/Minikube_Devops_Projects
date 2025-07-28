package com.example.demo.repository;

import com.example.demo.model.DataEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DataRepository extends JpaRepository<DataEntity, Long> {
}
