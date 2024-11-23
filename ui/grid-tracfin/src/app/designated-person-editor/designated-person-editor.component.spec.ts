import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DesignatedPersonEditorComponent } from './designated-person-editor.component';

describe('DesignatedPersonEditorComponent', () => {
  let component: DesignatedPersonEditorComponent;
  let fixture: ComponentFixture<DesignatedPersonEditorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DesignatedPersonEditorComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DesignatedPersonEditorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
